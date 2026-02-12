import numpy as np

def long_call(S, K, premium, lot):
    return lot * (np.maximum(S - K, 0) - premium)

def long_put(S, K, premium, lot):
    return lot * (np.maximum(K - S, 0) - premium)

def short_call(S, K, premium, lot):
    return lot * (premium - np.maximum(S - K, 0))

def short_put(S, K, premium, lot):
    return lot * (premium - np.maximum(K - S, 0))

def straddle(S, K, call_premium, put_premium, lot):
    return lot * (
        (np.maximum(S - K, 0) - call_premium) +
        (np.maximum(K - S, 0) - put_premium)
    )

def strangle(S, K1, K2, call_premium, put_premium, lot):
    return lot * (
        (np.maximum(S - K2, 0) - call_premium) +
        (np.maximum(K1 - S, 0) - put_premium)
    )
