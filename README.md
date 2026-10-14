# Statistical Analysis & Probability Programming Assignment

This repository contains all Python and R programs developed for the statistical analysis and probability modeling assignment.

---

## Project Structure

### Part I, Item 1: Factory Production & Defective Rate Calculator (Python)
* **File:** `SA1_Part1.py`
* **Objective:** Solves probability problems involving multiple manufacturing sources using user input and validation checks.
* **Features:**
  * Collects user input for production proportions ($x_i$) and ensures they satisfy validation rules ($0.10 \le x_i \le 0.40$ and sum to $1.0$)
  * Collects user input for defective rates ($y_i$) and ensures they satisfy validation rules ($0.01 \le y_i \le 0.05$ and sum to $0.12$)
  * Calculates the total probability that a randomly selected product is defective using the Law of Total Probability.

### Part I, Item 2: Interactive R Front-End for Discrete Random Variables (R)
* **File:** `SA1_Part2.R`
* **Objective:** Provides an interactive front-end console application in R for analyzing univariate and bivariate discrete random variables.
* **Features:**
  * **Univariate Analysis:** Computes the mean, variance, standard deviation, and cumulative distribution function (CDF), while plotting the PDF and CDF.
  * **Bivariate Analysis:** Accepts joint probability matrix inputs, computes marginal distributions, means, variances, and conditional distributions ($P(Y\vert{}X)$ and $P(X\vert{}Y)$), alongside marginal PDF plots.
  * **Validation Engine:** Strictly checks that all probabilities fall within $[0, 1]$ and sum precisely to $1.0$ (with error handling).

### Part I, Item 3: Search Engine Simulation Experiment (R)
* **File:** `SA1_Part3.R` (or similar)
* **Objective:** Carries out a Monte Carlo simulation experiment of 10,000 searches to analyze the geometric distribution and test the Markov memoryless property.
* **Features:**
  * Simulates search attempts until success using a default probability $p = 0.60$.
  * Computes simulated mean and variance against theoretical expectations.
  * Evaluates conditional distributions ($X - 3 \vert{} X > 3$) and verifies the memoryless property by comparing conditional probabilities like $P(X = 4 \vert{} X > 3)$ to baseline probabilities.

### Part II: Cryptocurrency Return Analysis (Python)
* **File:** `analysis.py`
* **Objective:** Analyzes cryptocurrency returns using probability distribution fitting and normality testing.
* **Features:**
  * **Bitcoin Distribution Fitting:** Dynamically simulates return structures and evaluates multiple standard probability distributions using the `fitter` library.
  * **Ethereum Normality Testing:** Samples high-frequency return datasets and runs the Shapiro-Wilk normality test.
---

## Prerequisites & Dependencies

### For Python Scripts:
```bash
pip install pandas numpy scipy fitter ccxt
