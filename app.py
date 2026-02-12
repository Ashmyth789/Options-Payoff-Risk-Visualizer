import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from strategies import *
from analytics import *

st.set_page_config(page_title="Options Payoff Visualizer")

st.title("📈 Options Payoff & Risk Visualizer")

strategy = st.selectbox(
    "Select Strategy",
    ["Long Call", "Long Put", "Short Call", "Short Put", "Straddle", "Strangle"]
)

spot = st.number_input("Current Spot Price", value=100.0)
lot = st.number_input("Lot Size", value=1)

S = np.linspace(spot * 0.5, spot * 1.5, 300)

if strategy in ["Long Call", "Long Put", "Short Call", "Short Put"]:
    K = st.number_input("Strike Price", value=100.0)
    premium = st.number_input("Premium", value=10.0)

elif strategy == "Straddle":
    K = st.number_input("Strike Price", value=100.0)
    call_premium = st.number_input("Call Premium", value=10.0)
    put_premium = st.number_input("Put Premium", value=10.0)

elif strategy == "Strangle":
    K1 = st.number_input("Put Strike (Lower)", value=90.0)
    K2 = st.number_input("Call Strike (Upper)", value=110.0)
    call_premium = st.number_input("Call Premium", value=8.0)
    put_premium = st.number_input("Put Premium", value=8.0)

if strategy == "Long Call":
    payoff = long_call(S, K, premium, lot)
    metrics = long_call_metrics(K, premium)

elif strategy == "Long Put":
    payoff = long_put(S, K, premium, lot)
    metrics = long_put_metrics(K, premium)

elif strategy == "Short Call":
    payoff = short_call(S, K, premium, lot)
    metrics = short_call_metrics(K, premium)

elif strategy == "Short Put":
    payoff = short_put(S, K, premium, lot)
    metrics = short_put_metrics(K, premium)

elif strategy == "Straddle":
    payoff = straddle(S, K, call_premium, put_premium, lot)
    metrics = {
        "Max Profit": "Unlimited",
        "Max Loss": call_premium + put_premium,
        "Breakeven": [K + call_premium + put_premium, K - (call_premium + put_premium)]
    }

elif strategy == "Strangle":
    payoff = strangle(S, K1, K2, call_premium, put_premium, lot)
    total_premium = call_premium + put_premium
    metrics = {
        "Max Profit": "Unlimited",
        "Max Loss": total_premium,
        "Breakeven": [K2 + total_premium, K1 - total_premium]
    }

fig, ax = plt.subplots()
ax.plot(S, payoff)
ax.axhline(0)
ax.set_xlabel("Underlying Price at Expiry")
ax.set_ylabel("Profit / Loss")
ax.set_title(strategy + " Payoff")
st.pyplot(fig)

st.subheader("📊 Strategy Metrics")
st.write(metrics)
