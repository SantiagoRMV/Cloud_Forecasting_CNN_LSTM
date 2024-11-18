from numpy import max, where

from Penalties.utils import NUMERIC


def hourly_payment(tolerance:float, real:NUMERIC, gx:NUMERIC, offer_price:NUMERIC, stock_price:NUMERIC) -> NUMERIC:
    return where(((gx*(1-tolerance) > real) | (real > gx*(1+tolerance))),
                 abs(real - gx) * abs(offer_price - stock_price),
                 0.0).round(decimals=1)

def daily_payment(ahead:NUMERIC, today:NUMERIC) -> float:
    return max(a=[ahead.sum(), today.sum()])