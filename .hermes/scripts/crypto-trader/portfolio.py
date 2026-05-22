"""Crypto Trading Pipeline - Portfolio Manager

Simulated portfolio management with £10,000 capital and 1% risk per trade.
Tracks positions, P&L, and generates orders for signals >= 8/10.
"""

import json
import time
import os
from datetime import datetime

PORTFOLIO_FILE = '.hermes/scripts/crypto-trader/portfolio_state.json'


def load_portfolio():
    """Load or initialize the simulated portfolio."""
    if os.path.exists(PORTFOLIO_FILE):
        try:
            with open(PORTFOLIO_FILE) as f:
                return json.load(f)
        except:
            pass
    return {
        'initial_capital': 10000.0,
        'cash': 10000.0,
        'positions': [],
        'trade_history': [],
        'total_trades': 0,
        'winning_trades': 0,
        'losing_trades': 0,
        'total_pnl': 0.0,
        'last_updated': datetime.utcnow().isoformat()
    }


def save_portfolio(portfolio):
    """Persist portfolio state."""
    portfolio['last_updated'] = datetime.utcnow().isoformat()
    os.makedirs(os.path.dirname(PORTFOLIO_FILE), exist_ok=True)
    with open(PORTFOLIO_FILE, 'w') as f:
        json.dump(portfolio, f, indent=2)


def execute_trades(signals, config, market_data):
    """
    Execute trades for signals meeting the threshold.
    Uses 1% risk per trade of current portfolio value.
    """
    portfolio = load_portfolio()
    executed = []
    min_score = config['scoring']['min_execution_score']
    risk_pct = config['portfolio']['risk_per_trade']
    max_positions = config['portfolio']['max_concurrent_positions']

    # Get open position pairs
    open_pairs = {p['pair'] for p in portfolio['positions']}

    for signal in signals:
        if not signal['execute']:
            continue
        if signal['score'] < min_score:
            continue
        if signal['pair'] in open_pairs:
            print(f"    ⚠ {signal['pair']}: Already in position, skipping")
            continue
        if len(portfolio['positions']) >= max_positions:
            print(f"    ⚠ Max concurrent positions ({max_positions}) reached, skipping {signal['pair']}")
            continue

        # Calculate position size: 1% risk
        risk_amount = portfolio['cash'] * risk_pct
        price = signal['current_price']

        if price <= 0 or risk_amount <= 5:  # Skip if too small
            continue

        # Simple position sizing: 1% of portfolio at current price
        # No leverage, spot-only
        quantity = round(risk_amount / price, 6)
        position_value = quantity * price

        if position_value > portfolio['cash']:
            continue

        # Create position
        position = {
            'pair': signal['pair'],
            'type': signal['direction'],
            'entry_price': price,
            'quantity': quantity,
            'value': position_value,
            'entry_score': signal['score'],
            'entry_time': datetime.utcnow().isoformat(),
            'stop_loss': None,  # To be calculated
            'take_profit': None,
            'timeframes': {tf: s['weighted_score'] for tf, s in signal['timeframes'].items()}
        }

        # Set stop loss at 2% below entry, take profit at 4% above (for longs)
        if signal['direction'] == 'LONG':
            position['stop_loss'] = round(price * 0.98, 6)
            position['take_profit'] = round(price * 1.04, 6)
        elif signal['direction'] == 'SHORT':
            position['stop_loss'] = round(price * 1.02, 6)
            position['take_profit'] = round(price * 0.96, 6)

        portfolio['cash'] -= position_value
        portfolio['positions'].append(position)

        trade_record = {
            'id': portfolio['total_trades'] + 1,
            'pair': signal['pair'],
            'type': signal['direction'],
            'entry_price': price,
            'quantity': quantity,
            'value': position_value,
            'score': signal['score'],
            'status': 'OPEN',
            'entry_time': datetime.utcnow().isoformat()
        }
        portfolio['trade_history'].append(trade_record)
        portfolio['total_trades'] += 1

        executed.append({
            'pair': signal['pair'],
            'direction': signal['direction'],
            'entry_price': price,
            'quantity': quantity,
            'value': position_value,
            'score': signal['score']
        })

        print(f"    ✅ EXECUTED: {signal['pair']} {signal['direction']} @ ${price:.4f} x {quantity} = ${position_value:.2f}")

    save_portfolio(portfolio)
    return portfolio, executed


def close_positions(portfolio, market_data):
    """Check and close any positions that hit stop/take-profit."""
    closed = []
    still_open = []

    for pos in portfolio['positions']:
        pair = pos['pair']
        tf_data = market_data.get(pair, {})
        latest_tf = '5M'
        candles = tf_data.get(latest_tf, [])
        if not candles:
            still_open.append(pos)
            continue

        current_price = candles[-1]['close']
        pnl_pct = ((current_price - pos['entry_price']) / pos['entry_price']) * 100

        # Check exits
        should_close = False
        exit_reason = ''

        if pos['type'] == 'LONG':
            if pos['stop_loss'] and current_price <= pos['stop_loss']:
                should_close = True
                exit_reason = 'STOP_LOSS'
            elif pos['take_profit'] and current_price >= pos['take_profit']:
                should_close = True
                exit_reason = 'TAKE_PROFIT'
        elif pos['type'] == 'SHORT':
            if pos['stop_loss'] and current_price >= pos['stop_loss']:
                should_close = True
                exit_reason = 'STOP_LOSS'
            elif pos['take_profit'] and current_price <= pos['take_profit']:
                should_close = True
                exit_reason = 'TAKE_PROFIT'

        # Also close if score drops significantly (trailing)
        if not should_close and abs(pnl_pct) >= 1.5:
            # Partial profit taking or stop
            pass

        if should_close:
            pnl_value = (current_price - pos['entry_price']) * pos['quantity'] if pos['type'] == 'LONG' else (pos['entry_price'] - current_price) * pos['quantity']
            portfolio['cash'] += (pos['quantity'] * current_price)

            closed.append({
                'pair': pair,
                'type': pos['type'],
                'entry': pos['entry_price'],
                'exit': current_price,
                'pnl_pct': round(pnl_pct, 2),
                'pnl_value': round(pnl_value, 2),
                'reason': exit_reason,
                'score': pos['entry_score']
            })

            if pnl_value > 0:
                portfolio['winning_trades'] += 1
            else:
                portfolio['losing_trades'] += 1
            portfolio['total_pnl'] += pnl_value

            print(f"    🔒 CLOSED: {pair} - {exit_reason} - PnL: ${pnl_value:.2f} ({pnl_pct:+.2f}%)")
        else:
            still_open.append(pos)

    portfolio['positions'] = still_open
    save_portfolio(portfolio)
    return portfolio, closed


def get_portfolio_summary(portfolio):
    """Get a nice portfolio summary."""
    total_equity = portfolio['cash'] + sum(
        p['value'] for p in portfolio['positions']
    ) if portfolio['positions'] else portfolio['cash']

    return {
        'initial_capital': portfolio['initial_capital'],
        'cash': round(portfolio['cash'], 2),
        'positions_value': round(sum(p['value'] for p in portfolio['positions']), 2) if portfolio['positions'] else 0,
        'total_equity': round(total_equity, 2),
        'total_pnl': round(portfolio['total_pnl'], 2),
        'total_pnl_pct': round((portfolio['total_pnl'] / portfolio['initial_capital']) * 100, 2),
        'open_positions': len(portfolio['positions']),
        'total_trades': portfolio['total_trades'],
        'win_rate': round((portfolio['winning_trades'] / max(portfolio['total_trades'], 1)) * 100, 1),
        'winning_trades': portfolio['winning_trades'],
        'losing_trades': portfolio['losing_trades']
    }
