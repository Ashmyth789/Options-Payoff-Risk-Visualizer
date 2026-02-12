def long_call_metrics(K, premium):
    return {
        "Max Profit": "Unlimited",
        "Max Loss": premium,
        "Breakeven": K + premium
    }

def long_put_metrics(K, premium):
    return {
        "Max Profit": K - premium,
        "Max Loss": premium,
        "Breakeven": K - premium
    }

def short_call_metrics(K, premium):
    return {
        "Max Profit": premium,
        "Max Loss": "Unlimited",
        "Breakeven": K + premium
    }

def short_put_metrics(K, premium):
    return {
        "Max Profit": premium,
        "Max Loss": K - premium,
        "Breakeven": K - premium
    }
