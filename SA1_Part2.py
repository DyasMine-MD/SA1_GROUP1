import pandas as pd
import numpy as np
from scipy import stats
from fitter import Fitter
import ccxt

# Initialize exchange and symbol reference
exchange = ccxt.binance()
symbol = 'BTC/USDT'

# 1. Generate Bitcoin dataset and compute returns
np.random.seed(42)
btc_prices = 10000 * np.cumprod(1 + np.random.normal(0.00001, 0.002, 5000))
df_btc = pd.DataFrame({'close': btc_prices})
btc_returns = df_btc['close'].pct_change().dropna()

# 2. Fit probability distributions to Bitcoin returns
print("Running distribution fitting for Bitcoin...")
f = Fitter(btc_returns.values)
f.fit()
print("--- Bitcoin Distribution Summary ---")
print(f.summary())

# 3. Generate Ethereum dataset and compute returns
eth_prices = 500 * np.cumprod(1 + np.random.normal(0.00001, 0.004, 5000))
df_eth = pd.DataFrame({'close': eth_prices})
eth_returns = df_eth['close'].pct_change().dropna()

# 4. Shapiro-Wilk Normality Test for Ethereum (sampled to 5000 points)
eth_sample = eth_returns.sample(n=5000, random_state=42)
stat, p_value = stats.shapiro(eth_sample)

print("\n--- Ethereum Shapiro-Wilk Test ---")
print(f"Shapiro-Wilk Statistic: {stat}, P-value: {p_value}")
