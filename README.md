# Quantitative Risk & Multi-Sector Equity Research Portfolio

## Executive Overview
This repository serves as a centralized, professional investment research showcase designed for buy-side recruitment. It contains an end-to-end framework combining rigorous quantitative risk/volatility engineering alongside highly structured fundamental long/short equity investment theses. 

The underlying assets span multiple uncorrelated sectors, demonstrating an advanced capacity to evaluate risk parameters, software moats, free cash flow (FCF) conversion loops, and corporate capital allocation strategies.

---

## 1. Quantitative Modeling & Volatility Infrastructure
* **Core Framework:** Advanced macro-scenario stress testing and daily implied volatility forecasting architecture.
* **Objective:** Engineering dynamic systematic parameters to evaluate capital downside under high-vix regimes, extreme macroeconomic shocks, and structural shifts in implied variance.
* **Core Methodologies:** Hybrid GARCH(1,1) implementations, time-series data alignment, and forward-looking variance modeling to map out multi-scenario portfolio drawdowns.

---

## 2. Investment Research & Active Asset Pitches

### 📊 Pitch #1: Nasdaq Inc. (NASDAQ: NDAQ)
* **Strategy:** Secular Growth / Structural Pivot
* **Thesis:** Analyzing the long-term corporate transition away from highly cyclical, volume-dependent transactional matching engines into a premium-multiple, recurring financial infrastructure SaaS business.
* **Artifacts:** `Nasdaq_Stock_Pitch_Tshepo_Ko...`

### 🚀 Pitch #2: Palantir Technologies (NASDAQ: PLTR)
* **Strategy:** High-Growth Enterprise Software Long
* **Thesis:** Capturing the mispriced velocity and operating leverage of the Artificial Intelligence Platform (AIP) deployment across the US Commercial ecosystem. Evaluates compressed customer acquisition costs (CAC) against massive recurring margins.
* **Artifacts:** `Palantir_Long_Pitch_Model.csv` | `PLTR_Stock_Pitch`

### 🚗 Pitch #3: General Motors (NYSE: GM)
* **Strategy:** Deep-Value / Contrarian Cash Flow Long
* **Thesis:** Exploiting an extreme valuation disconnect driven by surface-level electric vehicle transition friction. Highlights the massive, highly insulated free cash flow generation of legacy internal combustion engine (ICE) segments coupled with an aggressive $6.0B equity share repurchase program.
* **Artifacts:** `GM_Value_Pitch_Model.csv` | `GM_Stock_Pitch.md`

---

## 3. Institutional Execution Standards
All data sets, valuation matrix models, and qualitative investment memos are formatted strictly to buy-side presentation standards:
1. **`.csv` Layouts:** Configured explicitly to auto-render as clean, scannable, two-column grid data tables natively inside GitHub interfaces.
2. **`.md` Investment Notes:** Written utilizing standard investment banking/hedge fund nomenclature—focusing entirely on variant perception, execution catalysts, and margin of safety verification.


---

## 4. Complementary Optimization Tools (portfolio_optimizer.py)

In addition to the active asset pitches above, this repository includes an institutional-grade asset allocation framework built in Python utilizing Modern Portfolio Theory (MPT). 

The tool executes a Monte Carlo simulation across a diversified asset class basket to map out the Efficient Frontier and isolate the optimal allocation weights that maximize the portfolio's Sharpe Ratio.

### Core Portfolio Mechanics:
* **Expected Return:** Calculates the weighted sum of expected asset returns across the matrix.
* **Portfolio Volatility:** Captures total systemic risk using the structural asset covariance matrix to measure co-movements.
* **Sharpe Ratio Maximization:** Optimizes risk-adjusted excess returns over a baseline risk-free rate.

### Execution Parameters:
* **Asset Universe:** Proxy basket tracking Global Equities (SPY), Long-Term Treasuries (TLT), Gold (GLD), and Commodities (DBC).
* **Simulation Mechanics:** Generates 10,000 randomized, normalized weight vectors to determine long-only allocations.


---

## 5. Production Scaling & Local Execution

### 💡 API Data Sourcing Note
While this demonstration utilizes a static, annualized baseline covariance matrix for execution consistency, the underlying architecture is designed to ingest dynamic historical price feeds. In a live production environment, the engine can be integrated directly with institutional data endpoints (e.g., Bloomberg B-PIPE, Reuters Eikon, or wrappers like `yfinance`) to recalculate rolling covariance parameters in real-time.

### 💻 Quick Start & Dependencies
To clone this repository and execute the optimization model locally, run the following commands in your terminal:
<code>
git clone https://github.com/Tshepo-Stefan/Portfolio-Research.git
cd Portfolio-Research
pip install numpy
python portfolio_optimizer.py
</code>


