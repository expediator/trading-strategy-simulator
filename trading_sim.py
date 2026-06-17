import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# ---------- Config ----------
TICKER  = "NVDA"
START   = "2023-01-01"
END     = "2026-01-01"
CAPITAL = 10_000_000   # starting portfolio value

# ---------- Data ----------
data = yf.download(TICKER, start=START, end=END)

# ---------- Indicators ----------
data['SMA50']  = data['Close'].rolling(window=50).mean()
data['SMA200'] = data['Close'].rolling(window=200).mean()

# ---------- Signals ----------
data['Signal']   = 0
data.loc[data['SMA50'] > data['SMA200'], 'Signal'] =  1   # golden cross → buy
data.loc[data['SMA50'] < data['SMA200'], 'Signal'] = -1   # death cross  → sell
data['Position'] = data['Signal'].shift()

# ---------- Simulation ----------
money  = CAPITAL
shares = 0

for i in range(len(data)):
    pos   = data['Position'].iloc[i]
    price = data['Close'].iloc[i]
    if pos == 1 and money > 0:
        shares = money / price
        money  = 0
    elif pos == -1 and shares > 0:
        money  = shares * price
        shares = 0

final_value = money + shares * data['Close'].iloc[-1]

print(f"Ticker:        {TICKER}")
print(f"Period:        {START} → {END}")
print(f"Initial:       {CAPITAL:,.0f}")
print(f"Final value:   {float(final_value):,.2f}")
print(f"Return:        {(float(final_value)/CAPITAL - 1)*100:.2f}%")

# ---------- Plot ----------
plt.figure(figsize=(12, 6))
plt.title(f"{TICKER} — SMA50 vs SMA200 Crossover Strategy")
plt.plot(data['Close'],  label='Price',  linewidth=1.5)
plt.plot(data['SMA50'],  label='SMA 50', linewidth=1.2, linestyle='--')
plt.plot(data['SMA200'], label='SMA 200',linewidth=1.2, linestyle='--')
plt.legend()
plt.tight_layout()
plt.show()
