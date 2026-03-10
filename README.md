# 🛢️ Crude Oil Price Trend Analysis
### Brent & WTI Interactive Dashboard | Python + Plotly + yfinance

---

## 📌 Project Overview

This project analyzes **Brent Crude** and **WTI Crude** oil price data from 2019 to present, fetched live using the **Yahoo Finance API** via `yfinance`. It produces a fully interactive multi-panel dashboard covering price trends, moving averages, volatility, and the Brent–WTI spread.

**Why this matters:** Crude oil prices are the single most influential commodity price in the global economy — affecting everything from manufacturing costs and shipping rates to inflation and national budgets. Understanding price behavior is essential for analysts in energy, finance, logistics, and petrochemicals.

---

## 📊 What the Dashboard Shows

| Panel | Description |
|-------|-------------|
| **Brent Price + MAs** | Daily Brent price with 30-day and 90-day moving averages |
| **WTI Price + MAs** | Daily WTI price with 30-day and 90-day moving averages |
| **Brent vs WTI Comparison** | Side-by-side with key market event annotations |
| **Brent–WTI Spread** | The price premium Brent commands over WTI over time |
| **Brent Volatility** | 30-day annualised rolling volatility |
| **WTI Volatility** | 30-day annualised rolling volatility |

---

## 🔍 Key Findings

- **COVID-19 (March–April 2020):** Brent crashed from ~$65 to under $20. WTI briefly went **negative** (-$37) on April 20, 2020 — an unprecedented event caused by storage capacity limits.
- **Russia–Ukraine War (Feb 2022):** Brent surged to **~$128/barrel**, the highest level since 2008, driven by supply shock fears.
- **OPEC+ production cuts (2021–2023):** Sustained cuts helped stabilise prices and drive the 2021–2022 recovery.
- **Brent–WTI Spread:** Historically averages **$2–$5/barrel**, widening during geopolitical disruptions as Brent (global benchmark) reacts more sharply.
- **Volatility spikes** clearly correspond with major geopolitical and macroeconomic events.

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/crude-oil-analysis.git
cd crude-oil-analysis
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the analysis
```bash
python oil_analysis.py
```

This will:
- Fetch **live data** from Yahoo Finance API
- Generate `dashboard.html` in the same folder
- Print a summary of latest prices to the terminal

### 4. Open the dashboard
Open `dashboard.html` in any browser. You can zoom, hover, and pan all charts interactively.

---

## 🗂️ Project Structure

```
crude-oil-analysis/
├── oil_analysis.py       ← Main script (fetches live data + builds dashboard)
├── dashboard.html        ← Output: interactive Plotly dashboard
├── requirements.txt      ← Python dependencies
└── README.md             ← This file
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| `yfinance` | Fetches live oil futures prices from Yahoo Finance API |
| `pandas` | Data manipulation and indicator calculations |
| `plotly` | Interactive multi-panel dashboard |
| `numpy` | Numerical calculations |

---

## 📡 Data Source

- **Provider:** Yahoo Finance (via `yfinance` library)
- **Tickers:** `BZ=F` (Brent Crude Futures), `CL=F` (WTI Crude Futures)
- **Frequency:** Daily (business days)
- **Range:** January 2019 – Present (live, updates each run)

---

## 📈 Indicators Explained

**Moving Averages (30D & 90D):** Smooth out daily noise to reveal the underlying trend direction. A price above the 90-day MA signals a bullish trend; below signals bearish.

**Brent–WTI Spread:** Brent is the international benchmark; WTI is the US benchmark. The spread typically reflects US inventory levels, pipeline capacity, and geopolitical risk premiums.

**Annualised Volatility:** Calculated as the 30-day rolling standard deviation of daily returns, multiplied by √252. Higher = more uncertainty in the market.

---

*Built as part of a data analytics portfolio. Data sourced from Yahoo Finance.*
