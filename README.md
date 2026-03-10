# Crude Oil Price Trend Analysis
### Brent & WTI Interactive Dashboard | Python, Plotly, yfinance

---

## Overview

This project looks at Brent and WTI crude oil prices from 2019 to today. The data is pulled live from Yahoo Finance using the yfinance library, so every time you run the script you get the most current prices.

I built this to practice working with financial time series data and to better understand how the two main global oil benchmarks behave — and why they sometimes move differently.

The output is a single interactive HTML dashboard you can open in any browser.

**Author: Faisal Alsurayhi**

---

## What the Dashboard Shows

| Panel | Description |
|-------|-------------|
| Brent Price + MAs | Daily Brent price with 30-day and 90-day moving averages |
| WTI Price + MAs | Daily WTI price with 30-day and 90-day moving averages |
| Brent vs WTI Comparison | Both benchmarks on one chart with key event markers |
| Brent-WTI Spread | How much more expensive Brent is compared to WTI over time |
| Brent Volatility | 30-day rolling annualised volatility |
| WTI Volatility | 30-day rolling annualised volatility |

---

## Key Findings

- In April 2020, WTI oil briefly went negative — something that had never happened before. It was caused by a collapse in demand during COVID-19 combined with a storage crisis in the US.
- When Russia invaded Ukraine in February 2022, Brent shot up to around $128/barrel within weeks. It shows how sensitive oil markets are to supply disruptions.
- The Brent-WTI spread normally sits between $2-$5. When it widens sharply, it usually means something geopolitical is happening that affects global supply more than US supply.
- Volatility spikes line up almost perfectly with major world events — you can see the market panic and recovery just from the charts.

---

## How to Run

**1. Clone the repo**
```bash
git clone https://github.com/FaisalAlsurayhi/crude-oil-analysis.git
cd crude-oil-analysis
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the script**
```bash
python oil_analysis.py
```

This fetches live data, builds the dashboard, and opens it in your browser automatically.

---

## Project Structure

```
crude-oil-analysis/
├── oil_analysis.py       <- main script
├── dashboard.html        <- generated dashboard (open in browser)
├── requirements.txt      <- libraries needed
└── README.md
```

---

## Tech Stack

| Tool | What I used it for |
|------|-------------------|
| yfinance | Pulling live oil futures prices from Yahoo Finance API |
| pandas | Cleaning data and calculating indicators |
| plotly | Building the interactive dashboard |

---

## Data Source

- Yahoo Finance via yfinance
- Tickers: BZ=F (Brent Crude Futures), CL=F (WTI Crude Futures)
- Daily prices, January 2019 to present

---

## Indicators

**Moving Averages:** I used 30-day and 90-day MAs to smooth out daily noise and make the trend direction clearer. When price is above the 90-day MA, the market is generally in an uptrend.

**Brent-WTI Spread:** Brent is the global benchmark, WTI is the US one. The gap between them reflects things like US storage levels, pipeline capacity, and how much geopolitical risk is priced into global supply.

**Annualised Volatility:** Calculated using 30-day rolling standard deviation of daily returns multiplied by the square root of 252 (trading days in a year). Higher numbers mean the market is more uncertain.

---

*Part of my data analytics portfolio — Faisal Alsurayhi*
