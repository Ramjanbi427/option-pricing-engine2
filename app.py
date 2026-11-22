import streamlit as st
import numpy as np
from scipy.stats import norm

st.set_page_config(page_title="Option Pricing Engine", layout="centered")
st.title("Black-Scholes Option Pricing Engine")

# Sidebar inputs
st.sidebar.header("Model Parameters")
S = st.sidebar.number_input("Current Asset Price (S)", value=100.0, min_value=0.01)
K = st.sidebar.number_input("Strike Price (K)", value=100.0, min_value=0.01)
T = st.sidebar.number_input("Time to Maturity in Years (T)", value=1.0, min_value=0.01)
r = st.sidebar.number_input("Risk-Free Interest Rate (r)", value=0.05, format="%.4f")
sigma = st.sidebar.number_input("Volatility (σ)", value=0.20, min_value=0.01, format="%.4f")

# Black-Scholes Calculation
d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
d2 = d1 - sigma * np.sqrt(T)

call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
put_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

# Display Results
col1, col2 = st.columns(2)
col1.metric("Call Option Price", f"${call_price:.2f}")
col2.metric("Put Option Price", f"${put_price:.2f}") 