"""Crypto Trading Pipeline - HTML Report Generator

Generates beautiful, mobile-responsive HTML trading reports.
"""

import json
import os
from datetime import datetime


def _theme_css():
    return """
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #0a0e17;
            color: #e2e8f0;
            line-height: 1.6;
            padding: 20px;
        }
        .container { max-width: 1000px; margin: 0 auto; }
        .header {
            background: linear-gradient(135deg, #1a1f35, #0d1526);
            border: 1px solid #2a3a5c;
            border-radius: 16px;
            padding: 30px;
            margin-bottom: 24px;
        }
        .header h1 {
            font-size: 28px;
            background: linear-gradient(135deg, #60a5fa, #a78bfa);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 8px;
        }
        .header .subtitle { color: #94a3b8; font-size: 14px; }
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 16px;
            margin-bottom: 24px;
        }
        .stat-card {
            background: #111827;
            border: 1px solid #1e293b;
            border-radius: 12px;
            padding: 20px;
        }
        .stat-card .label { color: #64748b; font-size: 12px; text-transform: uppercase; letter-spacing: 0.5px; }
        .stat-card .value { font-size: 24px; font-weight: 700; margin-top: 4px; }
        .stat-card .value.positive { color: #22c55e; }
        .stat-card .value.negative { color: #ef4444; }
        .stat-card .value.neutral { color: #f59e0b; }
        .section-title {
            font-size: 18px;
            font-weight: 600;
            color: #f1f5f9;
            margin: 24px 0 16px;
            padding-bottom: 8px;
            border-bottom: 1px solid #1e293b;
        }
        .signal-card {
            background: #111827;
            border: 1px solid #1e293b;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 16px;
        }
        .signal-card.executable { border-color: #22c55e; box-shadow: 0 0 20px rgba(34,197,94,0.1); }
        .signal-card.hold { border-color: #f59e0b; }
        .signal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
        }
        .signal-header .pair { font-size: 18px; font-weight: 700; }
        .signal-header .score-badge {
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 14px;
            font-weight: 600;
        }
        .score-badge.high { background: rgba(34,197,94,0.15); color: #22c55e; }
        .score-badge.medium { background: rgba(245,158,11,0.15); color: #f59e0b; }
        .score-badge.low { background: rgba(239,68,68,0.15); color: #ef4444; }
        .signal-details {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
            gap: 8px;
            margin: 12px 0;
        }
        .signal-details .detail {
            background: #0d1526;
            padding: 8px 12px;
            border-radius: 8px;
            font-size: 13px;
        }
        .signal-details .detail .lbl { color: #64748b; }
        .tf-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 8px;
            margin-top: 12px;
        }
        .tf-card {
            background: #0d1526;
            border-radius: 8px;
            padding: 10px;
            text-align: center;
            font-size: 12px;
        }
        .tf-card .tf-label { color: #64748b; font-weight: 600; }
        .tf-card .tf-score { font-size: 16px; font-weight: 700; margin: 4px 0; }
        .tf-card .tf-score.good { color: #22c55e; }
        .tf-card .tf-score.ok { color: #f59e0b; }
        .tf-card .tf-score.bad { color: #ef4444; }
        .position-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 12px;
        }
        .position-table th {
            text-align: left;
            padding: 10px 12px;
            font-size: 12px;
            color: #64748b;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            border-bottom: 1px solid #1e293b;
        }
        .position-table td {
            padding: 10px 12px;
            font-size: 14px;
            border-bottom: 1px solid #1a1f35;
        }
        .badge {
            display: inline-block;
            padding: 2px 8px;
            border-radius: 12px;
            font-size: 11px;
            font-weight: 600;
        }
        .badge.open { background: rgba(59,130,246,0.15); color: #60a5fa; }
        .badge.win { background: rgba(34,197,94,0.15); color: #22c55e; }
        .badge.loss { background: rgba(239,68,68,0.15); color: #ef4444; }
        .badge.tp { background: rgba(34,197,94,0.15); color: #22c55e; }
        .badge.sl { background: rgba(239,68,68,0.15); color: #ef4444; }
        .footer {
            text-align: center;
            color: #475569;
            font-size: 12px;
            margin-top: 32px;
            padding: 20px;
            border-top: 1px solid #1e293b;
        }
        @media (max-width: 600px) {
            .tf-grid { grid-template-columns: repeat(2, 1fr); }
            .signal-details { grid-template-columns: repeat(2, 1fr); }
        }
    </style>
    """


def _score_color(score, max_score=10):
    ratio = score / max_score
    if ratio >= 0.8: return 'high'
    if ratio >= 0.5: return 'medium'
    return 'low'


def _tf_score_class(score, weight):
    ratio = score / weight if weight > 0 else 0
    if ratio >= 0.6: return 'good'
    if ratio >= 0.3: return 'ok'
    return 'bad'


def generate_report(signals, portfolio_summary, closed_trades, config):
    """Generate the full HTML report."""
    today = datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')
    date_str = datetime.utcnow().strftime('%Y-%m-%d')
    report = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crypto Trading Report - {date_str}</title>
    {_theme_css()}
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🤖 Advanced Crypto Trading Engine</h1>
            <div class="subtitle">
                Multi-Timeframe Analysis Pipeline • {today}<br>
                Capital: £{portfolio_summary['initial_capital']:,.2f} • Risk: {config['portfolio']['risk_per_trade']*100:.0f}%/trade
                • Min Score: {config['scoring']['min_execution_score']}/10
            </div>
        </div>
"""
    # Portfolio Stats
    pnl_class = 'positive' if portfolio_summary['total_pnl'] >= 0 else 'negative'
    report += f"""
        <div class="stats-grid">
            <div class="stat-card">
                <div class="label">Total Equity</div>
                <div class="value">£{portfolio_summary['total_equity']:,.2f}</div>
            </div>
            <div class="stat-card">
                <div class="label">Cash Available</div>
                <div class="value">£{portfolio_summary['cash']:,.2f}</div>
            </div>
            <div class="stat-card">
                <div class="label">Total P&amp;L</div>
                <div class="value {pnl_class}">{portfolio_summary['total_pnl_pct']:+.2f}% (${portfolio_summary['total_pnl']:+,.2f})</div>
            </div>
            <div class="stat-card">
                <div class="label">Win Rate</div>
                <div class="value">{portfolio_summary['win_rate']}%</div>
            </div>
            <div class="stat-card">
                <div class="label">Trades</div>
                <div class="value">{portfolio_summary['total_trades']} (W:{portfolio_summary['winning_trades']}/L:{portfolio_summary['losing_trades']})</div>
            </div>
            <div class="stat-card">
                <div class="label">Open Positions</div>
                <div class="value neutral">{portfolio_summary['open_positions']}</div>
            </div>
        </div>
"""

    # Trade Signals Section
    report += '<div class="section-title">📊 Trade Signals — Multi-Timeframe Analysis</div>\n'

    if not signals:
        report += '<div class="stat-card"><p style="color:#64748b;text-align:center;">No signals generated. Market data unavailable.</p></div>\n'
    else:
        for sig in signals:
            card_class = 'executable' if sig['execute'] else 'hold'
            score_class = _score_color(sig['score'])
            direction_icon = '🚀' if sig['direction'] == 'LONG' else '📉' if sig['direction'] == 'SHORT' else '⏸️'

            report += f"""
        <div class="signal-card {card_class}">
            <div class="signal-header">
                <div>
                    <span class="pair">{direction_icon} {sig['pair']}</span>
                    <span style="margin-left:8px;font-size:13px;color:#64748b;">{sig['direction']}</span>
                </div>
                <div>
                    <span class="score-badge {score_class}">{sig['score']}/{sig['max_score']} ({sig['score_pct']}%)</span>
                </div>
            </div>
            <div class="signal-details">
                <div class="detail"><span class="lbl">Price: </span>${sig['current_price']:.6f}</div>
                <div class="detail"><span class="lbl">Action: </span>{'✅ EXECUTE' if sig['execute'] else '⏳ HOLD'}</div>
            </div>
            <div class="tf-grid">
"""
            # Timeframe breakdown
            tf_order = ['4H', '1H', '15M', '5M']
            tf_labels = {'4H': 'Primary (4H)', '1H': 'Medium (1H)', '15M': 'Short (15M)', '5M': 'Precision (5M)'}
            for tf in tf_order:
                tf_info = sig['timeframes'].get(tf, {})
                tf_score = tf_info.get('weighted_score', 0)
                tf_max = tf_info.get('max_weighted', 1)
                tf_cls = _tf_score_class(tf_score, tf_max)
                details = tf_info.get('details', {})
                report += f"""
                <div class="tf-card">
                    <div class="tf-label">{tf_labels.get(tf, tf)}</div>
                    <div class="tf-score {tf_cls}">{tf_score:.1f}/{tf_max}</div>
                    <div style="color:#64748b;">
"""
                if details and details != 'No data':
                    report += f"RSI: {details.get('rsi_value', 'N/A')}<br>"
                    report += f"Vol: {details.get('vol_ratio', 'N/A')}x"
                report += """
                    </div>
                </div>
"""
            report += "</div></div>\n"

    # Closed Trades
    if closed_trades:
        report += '<div class="section-title">🔒 Closed Positions</div>\n'
        report += """
        <table class="position-table">
            <thead>
                <tr>
                    <th>Pair</th>
                    <th>Type</th>
                    <th>Entry</th>
                    <th>Exit</th>
                    <th>PnL</th>
                    <th>Reason</th>
                </tr>
            </thead>
            <tbody>
"""
        for t in closed_trades:
            pnl_cls = 'win' if t['pnl_value'] >= 0 else 'loss'
            badge_cls = 'tp' if t['reason'] == 'TAKE_PROFIT' else 'sl'
            report += f"""
                <tr>
                    <td><strong>{t['pair']}</strong></td>
                    <td>{t['type']}</td>
                    <td>${t['entry']:.4f}</td>
                    <td>${t['exit']:.4f}</td>
                    <td class="{pnl_cls}">{t['pnl_value']:+.2f} ({t['pnl_pct']:+.2f}%)</td>
                    <td><span class="badge {badge_cls}">{t['reason']}</span></td>
                </tr>
"""
        report += "</tbody></table>\n"

    # Analysis Methodology
    report += """
        <div class="section-title">⚙️ Analysis Methodology</div>
        <div style="background:#111827;border:1px solid #1e293b;border-radius:12px;padding:20px;font-size:13px;color:#94a3b8;">
            <p><strong>Timeframe Weighting:</strong> 4H (3pts) → 1H (3pts) → 15M (2pts) → 5M (2pts) = 10 total</p>
            <p><strong>Scoring Components (per timeframe):</strong> EMA Trend Alignment, RSI, MACD, Volume Surge, Bollinger Position</p>
            <p><strong>Execution:</strong> Signals ≥ 8/10 trigger trades with 1% risk allocation</p>
            <p><strong>Portfolio:</strong> £10,000 simulated starting capital, max 3 concurrent positions</p>
            <p><strong>Data Source:</strong> Binance Public API (free tier, no API key required)</p>
            <p style="margin-top:8px;color:#475569;"><em>⚠️ This is a simulated trading engine for educational purposes. Not financial advice.</em></p>
        </div>

        <div class="footer">
            Generated by Hermes Agent • {today}<br>
            Powered by Multi-Timeframe Technical Analysis
        </div>
    </div>
</body>
</html>"""

    return report


def save_report(report_html, config):
    """Save report to file and return the path."""
    date_str = datetime.utcnow().strftime('%Y-%m-%d')
    report_dir = config['output']['report_dir']
    os.makedirs(report_dir, exist_ok=True)
    filename = f"{config['output']['report_prefix']}-{date_str}.html"
    path = os.path.join(report_dir, filename)

    with open(path, 'w') as f:
        f.write(report_html)

    print(f"\n  📄 Report saved to: {path}")
    return path
