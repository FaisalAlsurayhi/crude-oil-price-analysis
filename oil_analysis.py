"""
Crude Oil Price Trend Analysis
================================
Fetches live Brent & WTI crude oil price data via yfinance API
and generates an interactive Plotly dashboard.

Author: [Your Name]
Data Source: Yahoo Finance (via yfinance)
"""

import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
from datetime import datetime, timedelta

# ──────────────────────────────────────────
# 1. FETCH DATA FROM YAHOO FINANCE API
# ──────────────────────────────────────────

print("📡 Fetching oil price data from Yahoo Finance API...")

START_DATE = "2019-01-01"
END_DATE   = datetime.today().strftime("%Y-%m-%d")

# BZ=F = Brent Crude Futures | CL=F = WTI Crude Futures
brent = yf.download("BZ=F", start=START_DATE, end=END_DATE, progress=False)
wti   = yf.download("CL=F", start=START_DATE, end=END_DATE, progress=False)

brent = brent[["Close"]].rename(columns={"Close": "Brent"})
wti   = wti[["Close"]].rename(columns={"Close": "WTI"})

df = pd.concat([brent, wti], axis=1).dropna()
df.index = pd.to_datetime(df.index)

print(f"✅ Data loaded: {len(df)} trading days ({START_DATE} → {END_DATE})")

# ──────────────────────────────────────────
# 2. CALCULATE INDICATORS
# ──────────────────────────────────────────

# Moving averages
df["Brent_MA30"]  = df["Brent"].rolling(30).mean()
df["Brent_MA90"]  = df["Brent"].rolling(90).mean()
df["WTI_MA30"]    = df["WTI"].rolling(30).mean()
df["WTI_MA90"]    = df["WTI"].rolling(90).mean()

# Spread (Brent premium over WTI)
df["Spread"] = df["Brent"] - df["WTI"]

# 30-day rolling volatility (annualised)
df["Brent_Volatility"] = df["Brent"].pct_change().rolling(30).std() * (252 ** 0.5) * 100
df["WTI_Volatility"]   = df["WTI"].pct_change().rolling(30).std() * (252 ** 0.5) * 100

# ──────────────────────────────────────────
# 3. KEY EVENTS FOR ANNOTATIONS
# ──────────────────────────────────────────

events = [
    {"date": "2020-03-09", "label": "Oil Price War<br>(Saudi-Russia)", "color": "#FF4B4B"},
    {"date": "2020-04-20", "label": "WTI Goes<br>Negative",           "color": "#FF4B4B"},
    {"date": "2021-01-01", "label": "OPEC+ Cuts<br>Extended",         "color": "#00C49A"},
    {"date": "2022-02-24", "label": "Russia-Ukraine<br>War",          "color": "#FF4B4B"},
    {"date": "2022-06-14", "label": "Price Peak<br>~$130",            "color": "#FFB347"},
    {"date": "2023-09-01", "label": "OPEC+ Extends<br>Cuts",          "color": "#00C49A"},
]

# ──────────────────────────────────────────
# 4. BUILD INTERACTIVE DASHBOARD
# ──────────────────────────────────────────

fig = make_subplots(
    rows=3, cols=2,
    subplot_titles=(
        "📈 Brent Crude — Price & Moving Averages",
        "📈 WTI Crude — Price & Moving Averages",
        "⚖️ Brent vs WTI Direct Comparison",
        "🔀 Brent–WTI Spread ($/barrel)",
        "📊 Brent Price Volatility (30-day annualised %)",
        "📊 WTI Price Volatility (30-day annualised %)",
    ),
    vertical_spacing=0.12,
    horizontal_spacing=0.08,
)

# ── COLORS ──
C_BRENT  = "#F4A900"
C_WTI    = "#00AEEF"
C_MA30   = "#FFFFFF"
C_MA90   = "#FF6B6B"
C_SPREAD = "#A78BFA"
C_VOL_B  = "#F4A900"
C_VOL_W  = "#00AEEF"
BG       = "#0D1117"
GRID     = "#1E2A3A"

# ── CHART 1: BRENT ──
fig.add_trace(go.Scatter(x=df.index, y=df["Brent"],
    name="Brent", line=dict(color=C_BRENT, width=1.5),
    hovertemplate="<b>Brent</b>: $%{y:.2f}<br>%{x|%d %b %Y}<extra></extra>"),
    row=1, col=1)
fig.add_trace(go.Scatter(x=df.index, y=df["Brent_MA30"],
    name="30-Day MA", line=dict(color=C_MA30, width=1, dash="dot"),
    hovertemplate="30D MA: $%{y:.2f}<extra></extra>"), row=1, col=1)
fig.add_trace(go.Scatter(x=df.index, y=df["Brent_MA90"],
    name="90-Day MA", line=dict(color=C_MA90, width=1.5, dash="dash"),
    hovertemplate="90D MA: $%{y:.2f}<extra></extra>"), row=1, col=1)

# ── CHART 2: WTI ──
fig.add_trace(go.Scatter(x=df.index, y=df["WTI"],
    name="WTI", line=dict(color=C_WTI, width=1.5),
    hovertemplate="<b>WTI</b>: $%{y:.2f}<br>%{x|%d %b %Y}<extra></extra>"),
    row=1, col=2)
fig.add_trace(go.Scatter(x=df.index, y=df["WTI_MA30"],
    name="30-Day MA", line=dict(color=C_MA30, width=1, dash="dot"),
    showlegend=False,
    hovertemplate="30D MA: $%{y:.2f}<extra></extra>"), row=1, col=2)
fig.add_trace(go.Scatter(x=df.index, y=df["WTI_MA90"],
    name="90-Day MA", line=dict(color=C_MA90, width=1.5, dash="dash"),
    showlegend=False,
    hovertemplate="90D MA: $%{y:.2f}<extra></extra>"), row=1, col=2)

# ── CHART 3: COMPARISON ──
fig.add_trace(go.Scatter(x=df.index, y=df["Brent"],
    name="Brent", line=dict(color=C_BRENT, width=2),
    showlegend=False,
    hovertemplate="<b>Brent</b>: $%{y:.2f}<extra></extra>"), row=2, col=1)
fig.add_trace(go.Scatter(x=df.index, y=df["WTI"],
    name="WTI", line=dict(color=C_WTI, width=2),
    showlegend=False,
    hovertemplate="<b>WTI</b>: $%{y:.2f}<extra></extra>"), row=2, col=1)

# ── CHART 4: SPREAD ──
fig.add_trace(go.Scatter(x=df.index, y=df["Spread"],
    name="Spread", fill="tozeroy",
    line=dict(color=C_SPREAD, width=1.5),
    fillcolor="rgba(167,139,250,0.15)",
    hovertemplate="<b>Spread</b>: $%{y:.2f}<extra></extra>"), row=2, col=2)
fig.add_hline(y=0, line_dash="dot", line_color="#555", row=2, col=2)

# ── CHART 5: BRENT VOLATILITY ──
fig.add_trace(go.Scatter(x=df.index, y=df["Brent_Volatility"],
    name="Brent Vol", fill="tozeroy",
    line=dict(color=C_VOL_B, width=1.5),
    fillcolor="rgba(244,169,0,0.15)",
    hovertemplate="<b>Brent Vol</b>: %{y:.1f}%<extra></extra>"), row=3, col=1)

# ── CHART 6: WTI VOLATILITY ──
fig.add_trace(go.Scatter(x=df.index, y=df["WTI_Volatility"],
    name="WTI Vol", fill="tozeroy",
    line=dict(color=C_VOL_W, width=1.5),
    fillcolor="rgba(0,174,239,0.15)",
    hovertemplate="<b>WTI Vol</b>: %{y:.1f}%<extra></extra>"), row=3, col=2)

# ── ADD EVENT ANNOTATIONS to the comparison chart ──
for ev in events:
    try:
        ev_date = pd.Timestamp(ev["date"])
        if ev_date in df.index:
            y_val = float(df.loc[ev_date, "Brent"])
        else:
            y_val = float(df["Brent"].iloc[df.index.get_indexer([ev_date], method="nearest")[0]])

        fig.add_vline(x=ev_date, line_dash="dot",
                      line_color=ev["color"], opacity=0.4, row=2, col=1)
        fig.add_annotation(
            x=ev_date, y=y_val + 8,
            text=ev["label"],
            showarrow=True, arrowhead=2,
            arrowcolor=ev["color"],
            font=dict(size=8, color=ev["color"]),
            bgcolor=BG, bordercolor=ev["color"],
            borderwidth=1, row=2, col=1
        )
    except Exception:
        pass

# ── SUMMARY STATS ──
latest_brent  = round(float(df["Brent"].iloc[-1]), 2)
latest_wti    = round(float(df["WTI"].iloc[-1]), 2)
latest_spread = round(float(df["Spread"].iloc[-1]), 2)
max_brent     = round(float(df["Brent"].max()), 2)
min_brent     = round(float(df["Brent"].min()), 2)
avg_spread    = round(float(df["Spread"].mean()), 2)

subtitle = (
    f"Latest: Brent ${latest_brent} | WTI ${latest_wti} | "
    f"Spread ${latest_spread}  ·  "
    f"Brent Range: ${min_brent} – ${max_brent}  ·  "
    f"Avg Spread: ${avg_spread}  ·  "
    f"Data: {START_DATE} → {END_DATE}"
)

# ── GLOBAL LAYOUT ──
fig.update_layout(
    title=dict(
        text="<b>CRUDE OIL MARKET ANALYSIS</b><br>"
             f"<span style='font-size:12px;color:#8B9BB4'>{subtitle}</span>",
        x=0.5, xanchor="center",
        font=dict(size=22, color="#F4A900", family="Georgia, serif")
    ),
    paper_bgcolor=BG,
    plot_bgcolor=BG,
    font=dict(color="#C9D1D9", family="'Courier New', monospace"),
    legend=dict(
        bgcolor="rgba(255,255,255,0.05)",
        bordercolor="#2E3A4E", borderwidth=1,
        font=dict(size=11)
    ),
    hovermode="x unified",
    height=1000,
    margin=dict(t=120, b=40, l=60, r=40),
)

# Axis styling
for i in range(1, 4):
    for j in range(1, 3):
        fig.update_xaxes(gridcolor=GRID, zerolinecolor=GRID,
                         showspikes=True, spikecolor="#444", row=i, col=j)
        fig.update_yaxes(gridcolor=GRID, zerolinecolor=GRID,
                         tickprefix="$", row=i, col=j)

# Volatility axes don't need $ prefix
fig.update_yaxes(tickprefix="", ticksuffix="%", row=3, col=1)
fig.update_yaxes(tickprefix="", ticksuffix="%", row=3, col=2)

# ── EXPORT ──
output_path = "dashboard.html"
pio.write_html(fig, file=output_path, auto_open=False,
               config={"displayModeBar": True, "scrollZoom": True})

print(f"\n✅ Dashboard saved → {output_path}")
print(f"   Open in your browser to explore the interactive charts.")
print(f"\n📊 Summary:")
print(f"   Brent (latest):  ${latest_brent}")
print(f"   WTI   (latest):  ${latest_wti}")
print(f"   Spread:          ${latest_spread}")
print(f"   Brent high/low:  ${max_brent} / ${min_brent}")
