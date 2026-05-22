"""Crypto Trading Pipeline - Market Data Fetcher (Free Tier)

Fetches OHLCV data from Binance public API (no API key needed for klines).
Supports all configured timeframes and trading pairs.
"""

import json
import time
import urllib.request
import urllib.error
from datetime import datetime, timedelta

BASE_URL = "https://api.binance.com/api/v3"


def fetch_klines(symbol, interval, limit=500):
    """Fetch OHLCV klines from Binance public API. No auth required."""
    url = f"{BASE_URL}/klines?symbol={symbol.replace('/', '')}&interval={interval}&limit={limit}"
    try:
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0')
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
        candles = []
        for k in data:
            candles.append({
                'timestamp': int(k[0]),
                'open': float(k[1]),
                'high': float(k[2]),
                'low': float(k[3]),
                'close': float(k[4]),
                'volume': float(k[5])
            })
        return candles
    except Exception as e:
        return None


def fetch_all_pairs(config, max_retries=3):
    """Fetch market data for all configured pairs across all timeframes."""
    pairs = config['pairs']
    timeframes = [config['timeframes'][k] for k in ['primary', 'secondary', 'tertiary', 'quaternary']]
    results = {}

    for pair in pairs:
        results[pair] = {}
        for tf in timeframes:
            for attempt in range(max_retries):
                candles = fetch_klines(pair, tf, limit=200)
                if candles:
                    results[pair][tf] = candles
                    print(f"  ✓ {pair} [{tf}]: {len(candles)} candles")
                    break
                else:
                    print(f"  ⚠ {pair} [{tf}]: attempt {attempt+1}/{max_retries} failed, retrying...")
                    time.sleep(2 ** attempt)
            else:
                print(f"  ✗ {pair} [{tf}]: all attempts failed")
                results[pair][tf] = []

    return results


def fetch_ticker_24hr(symbol):
    """Fetch 24hr ticker for current price/change data."""
    url = f"{BASE_URL}/ticker/24hr?symbol={symbol.replace('/', '')}"
    try:
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0')
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read().decode())
    except:
        return None
