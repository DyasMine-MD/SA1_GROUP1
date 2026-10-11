# Crypto Return Analysis: Distribution Fitting & Normality Testing

This repository contains a Python script built to analyze cryptocurrency market returns. It dives into statistical modeling by fitting probability distributions to Bitcoin data and running normality tests on Ethereum data[span_0](start_span)[span_0](end_span).

---

## What This Project Does

Since fetching years of high-frequency historical data live can hit API limits or missing file errors, this script dynamically simulates realistic market data to run two main statistical tasks:
1. **Bitcoin Distribution Fitting:** Tests multiple statistical distributions (like Gaussian, Student's t, etc.) against Bitcoin's 1-minute returns to find which model fits best using the `fitter` library[span_1](start_span)[span_1](end_span).
2. **Ethereum Normality Testing:** Samples Ethereum's 5-minute return dataset and runs the **Shapiro-Wilk test** to check if the data follows a normal distribution[span_2](start_span)[span_2](end_span).

---

## Prerequisites & Libraries

Make sure you have Python installed, along with these essential libraries for data science and stats:
```bash
pip install pandas numpy scipy fitter ccxt
