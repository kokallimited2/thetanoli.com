# Skills & Reference for Wadda Khan

Shared from Folio (2026-05-30). These skills live on Folio's machine — recreate on yours if needed.

## Key Skills

| Skill Name | Category | Content |
|------------|----------|---------|
| property-search-engine | projects | Full system: worker + frontend + scoring engine |
| property-data-api-research | projects | Complete API reference — endpoints, pricing, 36 strategy lists |

## Skill Content (For Manual Re-creation)

### property-search-engine

Two-form system: postcode search + single URL analysis. Cloudflare Worker backend.

**Scoring:** BRRR (35%) + BTL (30%) + Flip (35%) = Overall score. Verdict: STRONG_BUY 🟢 / BUY 🟡 / NEUTRAL 🟠 / PASS 🔴

**Files:** `~/property-search-engine/src/worker.js`, `src/analysis.js`, `public/index.html`

**API credits per search:** ~5 credits (1 sourcing + 4 area data)

### property-data-api-research

**36 strategy lists for sourced-properties endpoint:**
- BRRR/Flip: unmodernised-properties, derelict-properties, cheap-per-square-foot, repossessed-properties, auction-properties, slow-to-sell-properties, reduced-properties, back-on-market
- BTL: high-yield-properties, high-rental-demand, tenanted-properties-for-sale, hmo-licenced-properties
- Development: properties-with-planning-granted, land-plots-for-sale, suitable-for-splitting
- Location: walking-distance-to-town-centre, properties-near-a-university, near-large-development

**Key endpoints:** `/sourced-properties`, `/valuation-sale`, `/valuation-rent`, `/yields`, `/growth`, `/prices`, `/sold-prices`, `/rents`

## Full Property List (36 Total)

```
unmodernised-properties, repossessed-properties, cash-buyers-only-properties,
hmo-licenced-properties, investment-portfolios, cheap-per-square-foot,
quick-sale-properties, unbroken-freeholds, auction-properties,
reduced-properties, mixed-use, land-plots-for-sale, derelict-properties,
slow-to-sell-properties, large-properties, short-lease-properties,
two-to-three-bed-conversions, one-to-two-bed-conversions,
suitable-for-splitting, high-yield-properties, back-on-market,
tenanted-properties-for-sale, properties-with-planning-granted,
properties-on-a-corner-plot, holiday-let-properties, high-rental-demand,
properties-with-no-chain, poor-epc-score, properties-with-an-annexe,
bungalows-for-sale, georgian-houses, new-build-properties,
properties-with-good-views, near-green-space, properties-near-a-university,
walking-distance-to-town-centre, near-large-development,
properties-near-great-school, high-population-growth
```
