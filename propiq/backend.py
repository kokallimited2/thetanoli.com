#!/usr/bin/env python3
"""
PropIQ Backend — Property Intelligence Engine
Combines: PropertyData API + Deal Calculator + Rightmove URL Scraper

Usage:
  # Address lookup
  python3 backend.py --address "44 High Street, DY5 1LZ" --beds 3

  # Rightmove URL
  python3 backend.py --rightmove "https://www.rightmove.co.uk/properties/173277575"

  # Quick postcode
  python3 backend.py --postcode DY5 --beds 3 --price 200000

  # Output options
  python3 backend.py --address "DY5 1LZ" --output short
  python3 backend.py --address "DY5 1LZ" --output json
  python3 backend.py --address "DY5 1LZ" --output html
  python3 backend.py --address "DY5 1LZ" --output html --save ~/propiq-report.html
"""
import os, sys, json, re, math, html as html_mod
import urllib.request, urllib.error, urllib.parse
from datetime import datetime, timedelta
from typing import Optional

HOME = os.path.expanduser("~")
DATA_DIR = os.path.join(HOME, ".hermes", "data", "propiq")
os.makedirs(DATA_DIR, exist_ok=True)

# ──────────────────────────────────────────────
# PropertyData API Wrapper
# ──────────────────────────────────────────────
API_KEY = "TNK3PURKTE"
BASE = "https://api.propertydata.co.uk"

class PropertyDataAPI:
    """Thin wrapper around PropertyData.co.uk API with caching"""
    def __init__(self):
        self.cache_dir = os.path.join(DATA_DIR, "cache")
        os.makedirs(self.cache_dir, exist_ok=True)
        self.headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"}

    def _fetch(self, endpoint: str, postcode: str, limit: int = 50) -> dict:
        cache_key = f"{endpoint}_{postcode}_{limit}"
        cache_file = os.path.join(self.cache_dir, f"{cache_key}.json")
        # Check cache (< 1 hour old)
        if os.path.exists(cache_file):
            age = datetime.now() - datetime.fromtimestamp(os.path.getmtime(cache_file))
            if age < timedelta(hours=1):
                try:
                    with open(cache_file) as f:
                        return json.load(f)
                except: pass
        try:
            params = {"key": API_KEY, "postcode": postcode}
            if limit and endpoint in ("prices", "rents", "sold_prices"):
                params["limit"] = str(limit)
            qs = urllib.parse.urlencode(params)
            url = f"{BASE}/{endpoint}?{qs}"
            req = urllib.request.Request(url, headers=self.headers)
            with urllib.request.urlopen(req, timeout=20) as resp:
                data = json.loads(resp.read())
                with open(cache_file, "w") as f:
                    json.dump(data, f)
                return data
        except urllib.error.HTTPError as e:
            body = e.read().decode()
            return {"status": "error", "code": str(e.code), "message": body[:200]}
        except Exception as ex:
            return {"status": "error", "message": str(ex)[:200]}

    def prices(self, postcode: str) -> dict:
        return self._fetch("prices", postcode, limit=50)
    def yields(self, postcode: str) -> dict:
        return self._fetch("yields", postcode)
    def rents(self, postcode: str) -> dict:
        return self._fetch("rents", postcode, limit=50)
    def crime(self, postcode: str) -> dict:
        return self._fetch("crime", postcode)
    def sold_prices(self, postcode: str) -> dict:
        return self._fetch("sold_prices", postcode, limit=50)

# ──────────────────────────────────────────────
# Rightmove URL Parsing + Scraping
# ──────────────────────────────────────────────
RIGHTMOVE_PATTERNS = [
    re.compile(r'rightmove\.co\.uk/properties/(\d+)'),
    re.compile(r'rightmove\.co\.uk/(?:new-homes|commercial)/property-(\d+)'),
]

def parse_rightmove_url(url: str) -> Optional[int]:
    for pat in RIGHTMOVE_PATTERNS:
        m = pat.search(url)
        if m:
            return int(m.group(1))
    return None

def scrape_rightmove_listing(property_id: int, timeout: int = 15) -> dict:
    """Scrape a Rightmove listing page using __NEXT_DATA__ JSON"""
    url = f"https://www.rightmove.co.uk/properties/{property_id}"
    result = {"property_id": property_id, "url": url, "source": "rightmove"}
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
            "Accept": "text/html,application/xhtml+xml",
        })
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            html = resp.read().decode("utf-8", errors="replace")
        # Extract __NEXT_DATA__ JSON
        m = re.search(r'<script id="__NEXT_DATA__"[^>]*type="application/json"[^>]*>(.*?)</script>', html, re.DOTALL)
        if m:
            try:
                data = json.loads(m.group(1))
                props = data.get("props", {}).get("pageProps", {})
                listing = props.get("listing", {})
                # Price
                price_data = listing.get("price", {})
                if isinstance(price_data, dict):
                    price_str = price_data.get("display", "") or price_data.get("amount", "")
                else:
                    price_str = str(price_data)
                # Clean price string (£350,000 -> 350000)
                price = None
                if price_str:
                    price = int(re.sub(r'[^\d]', '', price_str)) if re.sub(r'[^\d]', '', price_str) else None
                # Beds
                bedrooms = listing.get("bedrooms")
                # Type
                property_type = listing.get("propertyType", "")
                # Address
                address_parts = listing.get("address", {})
                if isinstance(address_parts, dict):
                    display_address = address_parts.get("displayAddress", "")
                    postcode = address_parts.get("postalCode", "")
                else:
                    display_address = str(address_parts or "")
                    postcode = ""
                # Tenure
                tenure = listing.get("tenure", "")
                # Key features
                features = listing.get("keyFeatures", [])
                result.update({
                    "price": price,
                    "bedrooms": bedrooms,
                    "property_type": property_type,
                    "address": display_address,
                    "postcode": postcode,
                    "tenure": tenure,
                    "features": features,
                    "scraped": True,
                })
                return result
            except (json.JSONDecodeError, TypeError):
                pass
        # Fallback: regex extraction from HTML
        m_price = re.search(r'class="[^"]*price[^"]*"[^>]*>([^<]+)', html)
        if m_price:
            price_str = m_price.group(1).strip()
            price = int(re.sub(r'[^\d]', '', price_str)) if re.sub(r'[^\d]', '', price_str) else None
            result["price"] = price
        m_bed = re.search(r'(\d+)\s*bed(?:room)?s?\s*', html, re.IGNORECASE)
        if m_bed:
            result["bedrooms"] = int(m_bed.group(1))
        result["scraped"] = "price" in result or "bedrooms" in result
    except Exception as e:
        result["error"] = str(e)[:200]
    return result

# ──────────────────────────────────────────────
# Address Parsing
# ──────────────────────────────────────────────
POSTCODE_RE = re.compile(r'([A-Z]{1,2}\d{1,2}\s*\d[A-Z]{2}|[A-Z]{1,2}\d{1,2}[A-Z]?\s*\d[A-Z]{2})', re.IGNORECASE)
AREA_RE = re.compile(r'([A-Z]{1,2}\d{1,2})', re.IGNORECASE)

def extract_postcode(text: str) -> Optional[str]:
    m = POSTCODE_RE.search(text.upper())
    return m.group(1).strip().replace(" ", "")[:4] if m else None

def extract_area(text: str) -> Optional[str]:
    m = AREA_RE.search(text.upper())
    return m.group(1) if m else None

# ──────────────────────────────────────────────
# Deal Calculator Engine
# ──────────────────────────────────────────────
def round_py(val, d=0):
    return round(val, d)

def calculate_btl(price: float, rent: float, deposit_pct: float = 0.25,
                  interest_rate: float = 0.055, legals: float = 3000,
                  sdlt: float = None, mgmt_pct: float = 0.10) -> dict:
    """BTL calculator — returns score 0-10 + verdict"""
    rent_annual = rent * 12
    deposit = price * deposit_pct
    loan = price - deposit
    interest = loan * interest_rate
    sdlt = sdlt or (price * 0.05 if price > 250000 else price * 0.03)
    total_cost = deposit + sdlt + legals
    annual_costs = interest + rent_annual * mgmt_pct + rent_annual * 0.05  # voids + insurance
    net_income = rent_annual - annual_costs
    yield_pct = (net_income / total_cost * 100) if total_cost > 0 else 0
    # Scoring
    yi = yield_pct
    if yi >= 15: score = 10
    elif yi >= 12: score = 9
    elif yi >= 10: score = 8
    elif yi >= 8: score = 7
    elif yi >= 6: score = 6
    elif yi >= 5: score = 5
    elif yi >= 4: score = 4
    elif yi >= 3: score = 3
    elif yi >= 2: score = 2
    else: score = 1
    score += 0.5 if rent_annual * 1.5 > loan else 0  # coverage bonus
    score = min(score, 10)
    verdict = "Strong Buy" if score >= 8 else ("Consider" if score >= 6.5 else ("Watchlist" if score >= 5 else "Reject"))
    return {
        "score": round(score, 1), "yield_pct": round(yield_pct, 1),
        "net_income": round(net_income), "total_cost": round(total_cost),
        "rent_annual": round(rent_annual), "deposit": round(deposit),
        "sdlt": round(sdlt), "verdict": verdict,
    }

def calculate_brrr(purchase: float, refurb: float, arv: float, rent: float,
                   finance_rate: float = 0.08, legals: float = 4000) -> dict:
    """BRRR calculator — max score 10"""
    total_in = purchase + refurb + legals
    refi = arv * 0.75  # 75% LTV refinance
    cash_out = max(0, refi - total_in)
    left_in = max(0, total_in - refi)
    cash_on_cash = (rent * 12 / left_in * 100) if left_in > 0 else 999
    # Scoring based on cash-out + cash-on-cash
    if cash_out > 50000: score = 9
    elif cash_out > 30000: score = 8
    elif cash_out > 15000: score = 7
    elif cash_out > 5000: score = 6
    elif cash_out > 0: score = 5
    elif cash_on_cash > 15: score = 6
    elif cash_on_cash > 10: score = 5
    elif cash_on_cash > 5: score = 3
    else: score = 1
    score = min(score, 10)
    verdict = "Strong Buy" if score >= 8 else ("Consider" if score >= 6.5 else ("Watchlist" if score >= 4.5 else "Reject"))
    return {
        "score": round(score, 1), "total_in": round(total_in),
        "refi": round(refi), "cash_out": round(cash_out),
        "left_in": round(left_in), "cash_on_cash": round(cash_on_cash, 1),
        "verdict": verdict,
    }

def calculate_flip(purchase: float, refurb: float, arv: float,
                   sdlt: float = None, legals: float = 4000,
                   holding_months: int = 6, monthly_carry: float = 500) -> dict:
    """Flip calculator — max score 10"""
    sdlt = sdlt or (purchase * 0.05 if purchase > 250000 else purchase * 0.03)
    total_in = purchase + refurb + sdlt + legals + (holding_months * monthly_carry)
    gross_profit = arv - total_in
    margin = (gross_profit / arv * 100) if arv > 0 else 0
    stamp = sdlt + legals
    # Scoring
    if margin >= 25: score = 9
    elif margin >= 20: score = 8
    elif margin >= 15: score = 7
    elif margin >= 10: score = 6
    elif margin >= 7: score = 5
    elif margin >= 5: score = 4
    elif margin >= 3: score = 3
    else: score = 1
    # Penalise tight margins on low-value flips
    if gross_profit > 0 and gross_profit < 15000:
        score = max(1, score - 2)
    score = min(score, 10)
    verdict = "Strong Buy" if score >= 8 else ("Consider" if score >= 6.5 else ("Watchlist" if score >= 4.5 else "Reject"))
    return {
        "score": round(score, 1), "total_in": round(total_in),
        "gross_profit": round(gross_profit),
        "margin": round(margin, 1),
        "holding_costs": round(holding_months * monthly_carry),
        "verdict": verdict,
    }

# ──────────────────────────────────────────────
# Full Property Analysis
# ──────────────────────────────────────────────
def analyse_property(address: str = "", beds: int = None, price: float = None,
                     prop_type: str = None, rent_est: float = None,
                     refurb_est: float = None, rightmove_url: str = None) -> dict:
    """Main analysis pipeline — returns full dict with scores + area intel"""
    pd = PropertyDataAPI()
    postcode = extract_postcode(address or "")
    area = extract_area(address or "")

    # Handle Rightmove URL
    rightmove_data = None
    if rightmove_url:
        pid = parse_rightmove_url(rightmove_url)
        if pid:
            rightmove_data = scrape_rightmove_listing(pid)
            # Extract data from scraping
            if rightmove_data:
                price = price or rightmove_data.get("price")
                beds = beds or rightmove_data.get("bedrooms")
                prop_type = prop_type or rightmove_data.get("property_type")
                # Scrape address & postcode
                rm_addr = rightmove_data.get("address", "")
                rm_pc = rightmove_data.get("postcode", "")
                if rm_pc:
                    postcode = postcode or extract_postcode(rm_pc)
                if rm_addr and not address.strip():
                    address = rm_addr
                postcode = postcode or extract_postcode(rightmove_url)
                if not area:
                    area = extract_area(postcode or rightmove_url)

    # Derive area from postcode if we have one
    if not area and postcode:
        m = re.match(r'([A-Z]{1,2}\d{1,2})', postcode.upper().strip()[:4])
        if m:
            area = m.group(1)

    # Defaults
    avg_price = None
    yield_pct = None
    crime_rating = "Unknown"

    if area:
        prices_data = pd.prices(area)
        yields_data = pd.yields(area)
        rents_data = pd.rents(area)
        crime_data = pd.crime(area)
        sold_data = pd.sold_prices(area)

        # Extract price from PropertyData if not provided by Rightmove
        if not price and prices_data.get("status") == "success":
            avg_raw = prices_data.get("data", {}).get("average")
            if avg_raw and not beds:
                price = avg_raw
            else:
                props = prices_data.get("data", {}).get("raw_data", [])
                if props:
                    if beds:
                        matching = [p for p in props if p.get("bedrooms") == beds]
                        if matching:
                            p_prices = [p.get("price", 0) for p in matching if p.get("price")]
                            if p_prices:
                                price = int(sum(p_prices) / len(p_prices))
                            prop_type = prop_type or matching[0].get("type")
                    if not price:
                        p_prices = [p.get("price", 0) for p in props if p.get("price")]
                        if p_prices:
                            price = int(sum(p_prices) / len(p_prices))
                        beds = beds or props[0].get("bedrooms")
                        prop_type = prop_type or props[0].get("type")

        # Estimate rent from area
        if not rent_est and rents_data.get("status") == "success":
            rent_listings = rents_data.get("data", {}).get("raw_data", [])
            if rent_listings:
                rf_beds = [r for r in rent_listings if r.get("bedrooms") == beds] if beds else rent_listings
                if rf_beds:
                    r_prices = [r.get("price") for r in rf_beds if r.get("price")]
                    if r_prices:
                        rent_est = sum(r_prices) / len(r_prices)

        # Yield
        if yields_data.get("status") == "success":
            yield_pct = yields_data.get("data", {}).get("long_let", {}).get("gross_yield")

        # Avg area price
        if prices_data.get("status") == "success":
            avg_price = prices_data.get("data", {}).get("average")

        # Crime
        if crime_data.get("status") == "success":
            crime_rating = crime_data.get("data", {}).get("safety_rating", "Unknown")

    # Fallbacks
    if not price:
        price = 200000
    if not rent_est:
        rent_est = price * 0.006  # ~0.6% monthly rent rule
    if not refurb_est:
        refurb_est = 30000

    # Run calculators
    btl = calculate_btl(price, rent_est)
    brrr = calculate_brrr(price, refurb_est, price + refurb_est + 20000, rent_est)
    flip = calculate_flip(price, refurb_est, price + refurb_est * 2.5)

    # Area intel page check
    area_intel_path = os.path.join(HOME, "thetanoli.com", "dashboards", "nikka-intel",
                                    "area-intelligence", f"{area}-intel.html") if area else None
    has_area_page = os.path.exists(area_intel_path) if area_intel_path else False

    # Best strategy
    strategies = [("BTL", btl), ("BRRR", brrr), ("Flip", flip)]
    best = max(strategies, key=lambda s: s[1]["score"])

    return {
        "property": {
            "address": address or "Unknown",
            "postcode": postcode or "Unknown",
            "area": area,
            "price": round(price),
            "beds": beds,
            "type": prop_type or ("unknown" if not rightmove_data else "rightmove"),
            "estimated_rent": round(rent_est),
            "refurb_estimate": round(refurb_est),
            "rightmove_url": rightmove_url,
            "rightmove_scraped": rightmove_data.get("scraped", False) if rightmove_data else False,
        },
        "area": {
            "avg_price": round(avg_price) if avg_price else None,
            "gross_yield": yield_pct,
            "crime_rating": crime_rating,
            "has_area_intel_page": has_area_page,
        },
        "btl": btl,
        "brrr": brrr,
        "flip": flip,
        "best_strategy": best[0],
        "best_score": best[1]["score"],
        "best_verdict": best[1]["verdict"],
        "timestamp": datetime.now().isoformat(),
    }

# ──────────────────────────────────────────────
# HTML Report Generator
# ──────────────────────────────────────────────
def generate_report(analysis: dict, page_title: str = "PropIQ Report") -> str:
    """Return a full HTML page for the analysis"""
    p = analysis["property"]
    a = analysis["area"]
    btl = analysis["btl"]
    brrr = analysis["brrr"]
    flip = analysis["flip"]

    def score_bar(s):
        """Generate inline score bar"""
        c = "#f59e0b" if s >= 8 else ("#3b82f6" if s >= 6.5 else ("#64748b" if s >= 4.5 else "#ef4444"))
        return f'<div style="display:flex;align-items:center;gap:8px"><div style="flex:1;height:8px;background:#334155;border-radius:4px"><div style="width:{max(s*10, 5)}%;height:8px;background:{c};border-radius:4px"></div></div><strong style="color:{c};min-width:30px">{s}</strong></div>'

    rightmove_section = ""
    if p.get("rightmove_url"):
        src = "✅ Data scraped from listing" if p.get("rightmove_scraped") else "⚠️ Used estimate — listing may be dynamic"
        rightmove_section = f"""
<h2>Rightmove Source</h2>
<p><a href="{html_mod.escape(p['rightmove_url'])}" style="color:#3b82f6">{html_mod.escape(p['rightmove_url'])}</a></p>
<p>{src}</p>"""

    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html_mod.escape(page_title)}</title>
<style>
:root {{--bg:#0a0f1e;--card:#1e293b;--accent:#f59e0b;--text:#e2e8f0;--muted:#64748b;--success:#22c55e;--warn:#f59e0b;--danger:#ef4444;}}
* {{margin:0;padding:0;box-sizing:border-box}}
body {{background:var(--bg);color:var(--text);font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;padding:20px}}
.page-wrap {{max-width:1100px;margin:0 auto}}
h1 {{font-size:32px;margin-bottom:4px}}
h2 {{font-size:26px;margin:24px 0 8px}}
h3 {{font-size:18px;margin:12px 0 6px}}
.address {{color:var(--muted);font-size:16px;margin-bottom:16px}}
.card {{background:var(--card);border-radius:12px;padding:20px;margin-bottom:16px}}
.stat-row {{display:flex;gap:12px;flex-wrap:wrap;margin:12px 0}}
.stat {{background:#334155;border-radius:8px;padding:12px 16px;min-width:100px;flex:1}}
.stat-num {{font-size:28px;font-weight:700}}
.stat-label {{font-size:13px;color:var(--muted)}}
.strategy-grid {{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:12px}}
.strategy-card {{background:#334155;border-radius:10px;padding:16px;border-left:4px solid var(--accent)}}
.strategy-card strong {{font-size:18px}}
.verdict {{display:inline-block;padding:4px 12px;border-radius:20px;font-size:14px;font-weight:600}}
.verdict.strong-buy {{background:rgba(34,197,94,0.2);color:var(--success)}}
.verdict.consider {{background:rgba(59,130,246,0.2);color:#3b82f6}}
.verdict.watchlist {{background:rgba(100,116,139,0.2);color:var(--muted)}}
.verdict.reject {{background:rgba(239,68,68,0.2);color:var(--danger)}}
table {{width:100%;border-collapse:collapse;font-size:15px}}
th,td {{padding:8px 12px;text-align:left;border-bottom:1px solid #334155}}
th {{color:var(--muted);font-weight:600;font-size:13px}}
td {{color:var(--text)}}
footer {{color:var(--muted);font-size:13px;margin-top:32px;text-align:center}}
a {{color:#3b82f6}}
@media(max-width:600px){{.stat-row{{flex-direction:column}}}}
</style></head><body>
<div class="page-wrap">
<h1>🏠 PropIQ</h1>
<p class="address">{html_mod.escape(p["address"])} · {html_mod.escape(p.get("postcode",""))}
{ (" · <a href='" + html_mod.escape(p.get("rightmove_url","")) + "'>View on Rightmove</a>") if p.get("rightmove_url") else "" }</p>

<div class="stat-row">
<div class="stat"><div class="stat-num">£{p["price"]:,}</div><div class="stat-label">Target Price</div></div>
<div class="stat"><div class="stat-num">£{p["estimated_rent"]:,}<span style="font-size:16px;color:var(--muted)">/mo</span></div><div class="stat-label">Est. Rent</div></div>
<div class="stat"><div class="stat-num">{p["beds"] or "—"}</div><div class="stat-label">Bedrooms</div></div>
<div class="stat"><div class="stat-num">{p.get("type","—")[:12]}</div><div class="stat-label">Type</div></div>
</div>

<h2>Best Strategy: {analysis["best_strategy"]}</h2>
<div class="card">
<div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap">
<span style="font-size:24px;font-weight:700">{analysis["best_score"]}/10</span>
<span class="verdict {analysis['best_verdict'].lower().replace(' ','-')}">{analysis["best_verdict"]}</span>
</div>
{score_bar(analysis["best_score"])}
</div>

<h2>All Strategies</h2>
<div class="strategy-grid">
<div class="strategy-card">
<strong>💰 BTL</strong> {score_bar(btl["score"])}
<p style="margin-top:6px">Yield: {btl["yield_pct"]}% · Net: £{btl["net_income"]:,}/yr</p>
<span class="verdict {btl['verdict'].lower().replace(' ','-')}">{btl["verdict"]}</span>
</div>
<div class="strategy-card">
<strong>🔄 BRRR</strong> {score_bar(brrr["score"])}
<p style="margin-top:6px">Cash-out: £{brrr["cash_out"]:,} · CoC: {brrr["cash_on_cash"]}%</p>
<span class="verdict {brrr['verdict'].lower().replace(' ','-')}">{brrr["verdict"]}</span>
</div>
<div class="strategy-card">
<strong>🏗️ Flip</strong> {score_bar(flip["score"])}
<p style="margin-top:6px">Profit: £{flip["gross_profit"]:,} · Margin: {flip["margin"]}%</p>
<span class="verdict {flip['verdict'].lower().replace(' ','-')}">{flip["verdict"]}</span>
</div>
</div>

<h2>Area Intelligence</h2>
<table>
<tr><th>Metric</th><th>Value</th></tr>
<tr><td>Postcode Area</td><td>{a.get("area") or a.get("avg_price") and analysis["property"]["area"] or p.get("area") or "Unknown"}</td></tr>
<tr><td>Avg Area Price</td><td>{"£{:,.0f}".format(a["avg_price"]) if a["avg_price"] else "N/A"}</td></tr>
<tr><td>Gross Yield (Long Let)</td><td>{a["gross_yield"] or "N/A"}</td></tr>
<tr><td>Crime Safety</td><td>{a["crime_rating"] or "Unknown"}</td></tr>
{"<tr><td>Area Intel Page</td><td><a href='../area-intelligence/"+p['area']+"-intel.html' style='color:#3b82f6'>View Full Intel →</a></td></tr>" if a.get("has_area_intel_page") else ""}
</table>

{rightmove_section}

<footer>
PropIQ · Kokal Properties Ltd · Data from PropertyData.co.uk · Calculator v1.0<br>
<small>Generated {analysis["timestamp"][:19]}</small>
</footer>
</div></body></html>'''

# ──────────────────────────────────────────────
# CLI Entry Point
# ──────────────────────────────────────────────
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="PropIQ Property Analysis Engine")
    parser.add_argument("--address", help="Full UK property address")
    parser.add_argument("--rightmove", help="Rightmove listing URL")
    parser.add_argument("--postcode", help="Postcode for quick analysis")
    parser.add_argument("--beds", type=int, help="Number of bedrooms")
    parser.add_argument("--price", type=float, help="Property price")
    parser.add_argument("--type", dest="prop_type", help="Property type")
    parser.add_argument("--rent", type=float, help="Estimated monthly rent")
    parser.add_argument("--refurb", type=float, default=30000, help="Refurbishment estimate")
    parser.add_argument("--output", choices=["json", "html", "short"], default="json",
                        help="Output format (default: json)")
    parser.add_argument("--save", help="Save report to file path")
    args = parser.parse_args()

    if not any([args.address, args.rightmove, args.postcode]):
        parser.print_help()
        sys.exit(1)

    address = args.address or args.rightmove or args.postcode or ""
    analysis = analyse_property(
        address=address,
        beds=args.beds,
        price=args.price,
        prop_type=args.prop_type,
        rent_est=args.rent,
        refurb_est=args.refurb,
        rightmove_url=args.rightmove,
    )

    if args.output == "json" or (args.save and args.output not in ("html", "short")):
        output = json.dumps(analysis, indent=2)
        if args.save:
            with open(args.save, "w") as f:
                f.write(output)
            print(f"Saved JSON to {args.save}")
    elif args.output == "html":
        output = generate_report(analysis)
        if args.save:
            with open(args.save, "w") as f:
                f.write(output)
            print(f"Saved HTML to {args.save}")
    elif args.output == "short":
        p = analysis["property"]
        bs = analysis["best_strategy"]
        bv = analysis["best_verdict"]
        print(f"🏠 {p['address'][:60]}")
        print(f"   Best: {bs} — Score: {analysis['best_score']}/10 — Verdict: {bv}")
        print(f"   Price: £{p['price']:,} | Rent: £{p['estimated_rent']:,}/mo")
        print(f"   BTL: {analysis['btl']['score']}/10 | BRRR: {analysis['brrr']['score']}/10 | Flip: {analysis['flip']['score']}/10")
        output = ""

    if args.output != "short" or not args.save:
        print(output if args.output != "short" else "")
