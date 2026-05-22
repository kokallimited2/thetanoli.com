"""Crypto Trading Pipeline - Technical Indicator Calculator

Computes EMA, RSI, MACD, Bollinger Bands, Volume analysis.
All functions take list of dicts with OHLCV fields.
"""

import math


def _get_closes(candles):
    return [c['close'] for c in candles]


def _get_highs(candles):
    return [c['high'] for c in candles]


def _get_lows(candles):
    return [c['low'] for c in candles]


def _get_volumes(candles):
    return [c['volume'] for c in candles]


def ema(data, period):
    """Exponential Moving Average."""
    if len(data) < period:
        return None
    multiplier = 2 / (period + 1)
    result = [None] * (period - 1)
    sma = sum(data[:period]) / period
    result.append(sma)
    for i in range(period, len(data)):
        ema_val = (data[i] - result[-1]) * multiplier + result[-1]
        result.append(ema_val)
    return result


def sma(data, period):
    """Simple Moving Average."""
    if len(data) < period:
        return None
    result = []
    for i in range(len(data)):
        if i < period - 1:
            result.append(None)
        else:
            result.append(sum(data[i - period + 1:i + 1]) / period)
    return result


def rsi(candles, period=14):
    """Relative Strength Index."""
    closes = _get_closes(candles)
    if len(closes) < period + 1:
        return [None] * len(closes)

    gains, losses = [], []
    for i in range(1, len(closes)):
        diff = closes[i] - closes[i - 1]
        gains.append(diff if diff > 0 else 0)
        losses.append(-diff if diff < 0 else 0)

    result = [None] * period
    avg_gain = sum(gains[:period]) / period
    avg_loss = sum(losses[:period]) / period

    if avg_loss == 0:
        result.append(100.0)
    else:
        rs = avg_gain / avg_loss
        result.append(100 - (100 / (1 + rs)))

    for i in range(period, len(gains)):
        avg_gain = (avg_gain * (period - 1) + gains[i]) / period
        avg_loss = (avg_loss * (period - 1) + losses[i]) / period
        if avg_loss == 0:
            result.append(100.0)
        else:
            rs = avg_gain / avg_loss
            result.append(100 - (100 / (1 + rs)))

    return result


def macd(candles, fast=12, slow=26, signal=9):
    """MACD Line, Signal Line, and Histogram."""
    closes = _get_closes(candles)
    ema_fast = ema(closes, fast)
    ema_slow = ema(closes, slow)

    if not ema_fast or not ema_slow:
        return None, None, None

    macd_line = []
    for i in range(len(closes)):
        if ema_fast[i] is None or ema_slow[i] is None:
            macd_line.append(None)
        else:
            macd_line.append(ema_fast[i] - ema_slow[i])

    valid_macd = [m for m in macd_line if m is not None]
    if len(valid_macd) < signal:
        return macd_line, [None] * len(macd_line), [None] * len(macd_line)

    signal_line = ema([m if m is not None else 0 for m in macd_line], signal)
    # Rebuild with None alignment
    sig = [None] * (len(macd_line) - len(signal_line)) + signal_line

    hist = []
    for i in range(len(macd_line)):
        if macd_line[i] is not None and sig[i] is not None:
            hist.append(macd_line[i] - sig[i])
        else:
            hist.append(None)

    return macd_line, sig, hist


def bollinger_bands(candles, period=20, std_dev=2.0):
    """Bollinger Bands (upper, middle, lower)."""
    closes = _get_closes(candles)
    if len(closes) < period:
        return [None] * len(closes), [None] * len(closes), [None] * len(closes)

    mid = sma(closes, period)

    upper, lower = [], []
    for i in range(len(closes)):
        if mid[i] is None:
            upper.append(None)
            lower.append(None)
        else:
            segment = closes[i - period + 1:i + 1]
            variance = sum((x - mid[i]) ** 2 for x in segment) / period
            sd = math.sqrt(variance)
            upper.append(mid[i] + std_dev * sd)
            lower.append(mid[i] - std_dev * sd)

    return upper, mid, lower


def volume_ratio(candles, period=20):
    """Volume ratio: current volume / average volume."""
    volumes = _get_volumes(candles)
    if len(volumes) < period + 1:
        return 1.0
    avg_vol = sum(volumes[-period - 1:-1]) / period
    if avg_vol == 0:
        return 1.0
    return volumes[-1] / avg_vol


def atr(candles, period=14):
    """Average True Range for volatility measurement."""
    if len(candles) < period + 1:
        return None
    trs = []
    for i in range(1, len(candles)):
        hl = candles[i]['high'] - candles[i]['low']
        hc = abs(candles[i]['high'] - candles[i - 1]['close'])
        lc = abs(candles[i]['low'] - candles[i - 1]['close'])
        trs.append(max(hl, hc, lc))

    if len(trs) < period:
        return None
    return sum(trs[-period:]) / period
