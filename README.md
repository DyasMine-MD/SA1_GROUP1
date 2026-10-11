# Statistical Analysis & Probability Programming Assignment

This repository contains all Python and R programs developed for the statistical analysis and probability modeling assignment[span_2](start_span)[span_2](end_span)[span_3](start_span)[span_3](end_span).

---

## Project Structure

### Part I, Item 1: Factory Production & Defective Rate Calculator (Python)
* **File:** `SA1_Part1.py`
* **Objective:** Solves probability problems involving multiple manufacturing sources using user input and validation checks[span_4](start_span)[span_4](end_span).
* **Features:**
  * Collects user input for production proportions ($x_i$) and ensures they satisfy validation rules ($0.10 \le x_i \le 0.40$ and sum to $1.0$)[span_5](start_span)[span_5](end_span).
  * Collects user input for defective rates ($y_i$) and ensures they satisfy validation rules ($0.01 \le y_i \le 0.05$ and sum to $0.12$)[span_6](start_span)[span_6](end_span).
  * Calculates the total probability that a randomly selected product is defective using the Law of Total Probability[span_7](start_span)[span_7](end_span).

### Part I, Item 2: Interactive R Front-End for Discrete Random Variables (R)
* **File:** `SA1_Part2.R`
* **Objective:** Provides an interactive front-end console application in R for analyzing univariate and bivariate discrete random variables[span_8](start_span)[span_8](end_span).
* **Features:**
  * **Univariate Analysis:** Computes the mean, variance, standard deviation, and cumulative distribution function (CDF), while plotting the PDF and CDF[span_9](start_span)[span_9](end_span).
  * **Bivariate Analysis:** Accepts joint probability matrix inputs, computes marginal distributions, means, variances, and conditional distributions ($P(Y\vert{}X)$ and $P(X\vert{}Y)$), alongside marginal PDF plots[span_10](start_span)[span_10](end_span).
  * **Validation Engine:** Strictly checks that all probabilities fall within $[0, 1]$ and sum precisely to $1.0$ (with error handling)[span_11](start_span)[span_11](end_span).

### Part I, Item 3: Search Engine Simulation Experiment (R)
* **File:** `SA1_Part3.R` (or similar)
* **Objective:** Carries out a Monte Carlo simulation experiment of 10,000 searches to analyze the geometric distribution and test the Markov memoryless property[span_12](start_span)[span_12](end_span)[span_13](start_span)[span_13](end_span).
* **Features:**
  * Simulates search attempts until success using a default probability $p = 0.60$[span_14](start_span)[span_14](end_span)[span_15](start_span)[span_15](end_span).
  * Computes simulated mean and variance against theoretical expectations[span_16](start_span)[span_16](end_span).
  * Evaluates conditional distributions ($X - 3 \vert{} X > 3$) and verifies the memoryless property by comparing conditional probabilities like $P(X = 4 \vert{} X > 3)$ to baseline probabilities[span_17](start_span)[span_17](end_span)[span_18](start_span)[span_18](end_span).

### Part II: Cryptocurrency Return Analysis (Python)
* **File:** `analysis.py`
* **Objective:** Analyzes cryptocurrency returns using probability distribution fitting and normality testing[span_19](start_span)[span_19](end_span).
* **Features:**
  * **Bitcoin Distribution Fitting:** Dynamically simulates return structures and evaluates multiple standard probability distributions using the `fitter` library[span_20](start_span)[span_20](end_span).
  * **Ethereum Normality Testing:** Samples high-frequency return datasets and runs the Shapiro-Wilk normality test[span_21](start_span)[span_21](end_span).

---

## Prerequisites & Dependencies

### For Python Scripts:
```bash
pip install pandas numpy scipy fitter ccxt
