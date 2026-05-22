#!/usr/bin/env python3
"""
Advanced Crypto Trading Engine Pipeline
========================================
Multi-timeframe analysis (4H→1H→15M→5M) with trade scoring (≥8/10 to execute).
£10,000 simulated portfolio with 1% risk per trade.

Usage:
    python3 run_trader.py              # Full pipeline run
    python3 run_trader.py --html-only  # Regenerate report from cached data

Delivers: HTML report to Telegram and email.
"""

import json
import os
import sys
import time
from datetime import datetime

# Add parent to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_fetcher import fetch_all_pairs, fetch_ticker_24hr
from signals import generate_signals
from portfolio import execute_trades, close_positions, get_portfolio_summary, load_portfolio
from reporter import generate_report, save_report


def load_config():
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    if not os.path.exists(config_path):
        # Try relative from cwd
        config_path = '.hermes/scripts/crypto-trader/config.json'
    with open(config_path) as f:
        return json.load(f)


def run_pipeline(config):
    """Execute the full trading pipeline."""
    print("=" * 60)
    print("  ADVANCED CRYPTO TRADING ENGINE")
    print("  Multi-Timeframe Analysis Pipeline")
    print("=" * 60)
    print(f"\n  📅 {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}")
    print(f"  Portfolio: £{config['portfolio']['initial_capital']:,.2f}")
    print(f"  Risk: {config['portfolio']['risk_per_trade']*100:.0f}%/trade")
    print(f"  Min Score: {config['scoring']['min_execution_score']}/10")
    print(f"  Pairs: {', '.join(config['pairs'])}")
    print()

    # Step 1: Fetch market data
    print("📡 Step 1: Fetching Market Data...")
    start = time.time()
    market_data = fetch_all_pairs(config)
    elapsed = time.time() - start
    print(f"  Done in {elapsed:.1f}s\n")

    # Step 2: Generate signals
    print("📊 Step 2: Generating Trade Signals...")
    signals = generate_signals(market_data, config)
    print(f"\n  Total signals: {len(signals)}")
    print(f"  Executable (≥{config['scoring']['min_execution_score']}/10): {sum(1 for s in signals if s['execute'])}")

    # Step 3: Close existing positions if they hit targets
    print("\n🔒 Step 3: Managing Open Positions...")
    portfolio = load_portfolio()
    portfolio, closed_trades = close_positions(portfolio, market_data)
    print(f"  Closed today: {len(closed_trades)}")

    # Step 4: Execute new trades
    print("\n💰 Step 4: Executing New Trades...")
    portfolio, executed = execute_trades(signals, config, market_data)
    print(f"  New trades: {len(executed)}")

    # Step 5: Generate report
    print("\n📄 Step 5: Generating Report...")
    summary = get_portfolio_summary(portfolio)
    report_html = generate_report(signals, summary, closed_trades, config)
    report_path = save_report(report_html, config)
    
    print(f"\n{'=' * 60}")
    print(f"  PIPELINE COMPLETE")
    print(f"  Portfolio: £{summary['total_equity']:,.2f} ({summary['total_pnl_pct']:+}%)")
    print(f"  Report: {report_path}")
    print(f"{'=' * 60}\n")

    return report_path, report_html


def main():
    config = load_config()
    report_path, report_html = run_pipeline(config)
    
    # Output the report HTML path for delivery system
    print(f"\nREPORT_PATH:{report_path}")
    
    # Also output the HTML content for direct delivery
    with open(report_path) as f:
        html = f.read()
    print(f"\nREPORT_HTML_BELOW")
    print(html)


if __name__ == '__main__':
    main()
