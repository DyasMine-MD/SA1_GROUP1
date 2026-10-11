import pandas as pd
import numpy as np
from scipy import  stats
from fitter import Fitter
import ccxt
xchange = ccxt.binance()
symbol = 'BTC/USDT'
# Fetch data for Bitcoin from Binance
np.random.seed()
stat, p_value = stats.shapiro(eth_sample)
print(f"Shapiro-Wilk Stati3`stic: {stat}, P-value: {p_value}") 