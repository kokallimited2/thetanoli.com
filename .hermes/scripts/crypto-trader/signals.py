"""Crypto Trading Pipeline - Trade Signal Generator

Multi-timeframe analysis engine that scores trade setups.
- 4H (Primary trend): 3 points max
- 1H (Medium-term): 3 points max
- 15M (Short-term entry): 2 points max
- 5M (Precision filter): 2 points max
Total possible: 10 points. Minimum to execute: 8 points.
"""

import json
from . import indicators as ind


def _trend_direction(ema_9, ema_21, ema_50, ema_200, current_price):
    """Determine trend strength and direction from EMAs."""
    if None in (ema_9, ema_21, ema_50, ema_200):
        return 0
    score = 0
    # Alignment of EMAs (bullish: 9 > 21 > 50 > 200)
    if ema_9 > ema_21: score += 1
    if ema_21 > ema_50: score += 1
    if ema_50 > ema_200: score += 1
    # Price above all EMAs
    if current_price > ema_200: score += 1
    # Convert to -2 to +4 range (negative if bearish)
    return score


def _score_macd(macd_line, signal_line, histogram):
    """Score MACD setup. Max 2 points."""
    if macd_line is None or signal_line is None:
        return 0
    score = 0
    # MACD above signal line
    if macd_line > signal_line: score += 1
    # Histogram positive and increasing
    if histogram and histogram > 0: score += 0.5
    # MACD above zero line (strong momentum)
    if macd_line > 0: score += 0.5
    return score


def _score_rsi(rsi_val, rsi_oversold=30, rsi_overbought=70):
    """Score RSI. Max 1 point."""
    if rsi_val is None:
        return 0
    # Oversold (bullish) or just right momentum
    if rsi_val < rsi_oversold: return 1.0
    if rsi_val < 50: return 0.5
    if rsi_val > rsi_overbought: return 0  # Overbought = sell signal
    if rsi_val > 50: return 0.5
    return 0.3


def _score_volume(vol_ratio):
    """Score volume confirmation. Max 1 point."""
    if vol_ratio >= 1.5: return 1.0
    if vol_ratio >= 1.2: return 0.5
    if vol_ratio >= 1.0: return 0.2
    return 0


def _score_bb_position(close, bb_upper, bb_lower, bb_mid):
    """Score Bollinger Band position. Max 1 point."""
    if None in (bb_upper, bb_lower, bb_mid):
        return 0
    bb_range = bb_upper - bb_lower
    if bb_range == 0:
        return 0
    pos = (close - bb_lower) / bb_range
    # Sweet spot: between 0.3 and 0.7 (middle area, room to move)
    if 0.3 <= pos <= 0.7: return 1.0
    if 0.2 <= pos <= 0.8: return 0.5
    return 0.2


def analyze_timeframe(candles, config):
    """Full technical analysis for a single timeframe. Returns score components."""
    closes = [c['close'] for c in candles]
    if len(closes) < 50:
        return {'score': 0, 'signals': {'error': 'insufficient_data'}}

    cfg = config['indicators']
    current_price = closes[-1]

    # EMA
    ema_vals = {}
    for p in cfg['ema_periods']:
        vals = ind.ema(closes, p)
        ema_vals[p] = vals[-1] if vals and vals[-1] is not None else None

    # RSI
    rsi_vals = ind.rsi(candles, cfg['rsi_period'])
    rsi_val = rsi_vals[-1] if rsi_vals else None

    # MACD
    macd_line, sig_line, hist = ind.macd(
        candles, cfg['macd_fast'], cfg['macd_slow'], cfg['macd_signal']
    )
    macd_val = macd_line[-1] if macd_line and macd_line[-1] is not None else None
    sig_val = sig_line[-1] if sig_line and sig_line[-1] is not None else None
    hist_val = hist[-1] if hist and hist[-1] is not None else None

    # Bollinger Bands
    bb_u, bb_m, bb_l = ind.bollinger_bands(
        candles, cfg['bb_period'], cfg['bb_std']
    )

    # Volume
    vr = ind.volume_ratio(candles, cfg['volume_ma_period'])

    # Trend
    trend = _trend_direction(
        ema_vals[9], ema_vals[21], ema_vals[50], ema_vals[200],
        current_price
    )

    return {
        'score': 0,  # Will be weighted by caller
        'current_price': current_price,
        'ema_9': ema_vals[9],
        'ema_21': ema_vals[21],
        'ema_50': ema_vals[50],
        'ema_200': ema_vals[200],
        'rsi': rsi_val,
        'macd': macd_val,
        'macd_signal': sig_val,
        'macd_histogram': hist_val,
        'bb_upper': bb_u[-1] if bb_u else None,
        'bb_middle': bb_m[-1] if bb_m else None,
        'bb_lower': bb_l[-1] if bb_l else None,
        'volume_ratio': vr,
        'trend_score': trend,
        'close': current_price
    }


def score_setup(all_timeframes_data, config):
    """
    Multi-timeframe scoring engine.
    4H: 3pts | 1H: 3pts | 15M: 2pts | 5M: 2pts = 10 total
    Returns: (total_score, details_dict)
    """
    cfg = config['indicators']
    weights = {
        '4H': 3,   # Primary trend
        '1H': 3,   # Medium-term alignment
        '15M': 2,  # Short-term entry
        '5M': 2    # Precision filter
    }

    tf_scores = {}
    total_score = 0
    max_possible = 0

    for tf, weight in weights.items():
        data = all_timeframes_data.get(tf)
        if not data or 'score' not in data:
            tf_scores[tf] = {
                'weight': weight,
                'raw_score': 0,
                'weighted_score': 0,
                'details': 'No data'
            }
            continue

        closes = [c['close'] for c in data]
        current_price = closes[-1]

        # Component scoring
        ema_9, ema_21, ema_50, ema_200 = None, None, None, None
        rsi_val = ind.rsi(data, cfg['rsi_period'])
        rsi_val = rsi_val[-1] if rsi_val else None

        closes_list = [c['close'] for c in data]
        for p in cfg['ema_periods']:
            vals = ind.ema(closes_list, p)
            if p == 9: ema_9 = vals[-1] if vals else None
            if p == 21: ema_21 = vals[-1] if vals else None
            if p == 50: ema_50 = vals[-1] if vals else None
            if p == 200: ema_200 = vals[-1] if vals else None

        macd_l, macd_s, macd_h = ind.macd(data, cfg['macd_fast'], cfg['macd_slow'], cfg['macd_signal'])
        macd_val = macd_l[-1] if macd_l else None
        sig_val = macd_s[-1] if macd_s else None
        hist_val = macd_h[-1] if macd_h else None

        bb_u, bb_m, bb_l = ind.bollinger_bands(data, cfg['bb_period'], cfg['bb_std'])
        vr = ind.volume_ratio(data, cfg['volume_ma_period'])

        # 1. Trend (EMA alignment) - max 1 per TF
        trend_pts = 0
        if ema_9 and ema_21 and ema_50:
            if ema_9 > ema_21: trend_pts += 0.4
            if ema_21 > ema_50: trend_pts += 0.3
            if current_price > ema_50: trend_pts += 0.3

        # 2. RSI - max 0.5 per TF
        rsi_pts = 0
        if rsi_val is not None:
            if rsi_val < 35: rsi_pts = 0.5  # Oversold bounce setup
            elif 35 <= rsi_val <= 55: rsi_pts = 0.3  # Neutral zone
            elif rsi_val > 75: rsi_pts = 0  # Overbought, avoid

        # 3. MACD - max 0.5 per TF
        macd_pts = 0
        if macd_val is not None and sig_val is not None:
            if macd_val > sig_val: macd_pts += 0.3
            if macd_val > 0: macd_pts += 0.2

        # 4. Volume - max 0.5 per TF
        vol_pts = 0
        if vr >= 1.5: vol_pts = 0.5
        elif vr >= 1.2: vol_pts = 0.3
        elif vr >= 1.0: vol_pts = 0.1

        # 5. Bollinger Bands position - max 0.5 per TF
        bb_pts = 0
        if bb_u[-1] is not None and bb_l[-1] is not None:
            pos = (current_price - bb_l[-1]) / (bb_u[-1] - bb_l[-1]) if (bb_u[-1] - bb_l[-1]) > 0 else 0.5
            if 0.2 <= pos <= 0.5: bb_pts = 0.5  # Near lower band, potential bounce
            elif 0.5 < pos <= 0.7: bb_pts = 0.3

        raw = trend_pts + rsi_pts + macd_pts + vol_pts + bb_pts
        # Scale to weight's max
        weighted = (raw / 3.0) * weight

        tf_scores[tf] = {
            'weight': weight,
            'raw_score': round(raw, 2),
            'weighted_score': round(weighted, 2),
            'max_weighted': weight,
            'details': {
                'price': round(current_price, 6),
                'trend': round(trend_pts, 2),
                'rsi': round(rsi_pts, 2) if rsi_pts else 0,
                'rsi_value': round(rsi_val, 1) if rsi_val else None,
                'macd': round(macd_pts, 2),
                'volume': round(vol_pts, 2),
                'bb': round(bb_pts, 2),
                'vol_ratio': round(vr, 2)
            }
        }

        total_score += weighted
        max_possible += weight

    return total_score, tf_scores


def generate_signals(market_data, config):
    """Generate trade signals for all pairs. Returns ranked list."""
    signals = []
    for pair, tf_data in market_data.items():
        print(f"\n  Analyzing {pair}...")
        has_data = all(len(tf_data.get(tf, [])) > 50 for tf in ['4H', '1H', '15M', '5M'])
        if not has_data:
            print(f"    ⚠ Insufficient data, skipping")
            continue

        total_score, tf_scores = score_setup(tf_data, config)

        # Get latest prices for context
        latest = tf_data['5M'][-1] if tf_data.get('5M') else tf_data.get('1H', [{}])[-1]
        current_price = latest.get('close', 0)

        signals.append({
            'pair': pair,
            'score': round(total_score, 2),
            'score_pct': round((total_score / 10) * 100, 1),
            'max_score': 10,
            'execute': total_score >= config['scoring']['min_execution_score'],
            'current_price': current_price,
            'timeframes': tf_scores,
            'direction': 'LONG' if total_score >= 5 else 'SHORT' if total_score <= 3 else 'NEUTRAL',
            'timestamp': latest.get('timestamp', 0)
        })

        print(f"    Score: {total_score:.2f}/10 {'🚀 EXECUTE' if total_score >= 8 else '⏳ HOLD'}")

    # Sort by score descending
    signals.sort(key=lambda s: s['score'], reverse=True)
    return signals
