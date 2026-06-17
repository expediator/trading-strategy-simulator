# 📈 Trading Strategy Simulator

Backtests a classic **SMA 50/200 golden-cross strategy** on real stock data using Yahoo Finance, then outputs a P&L report and price chart.

**Source:** [github.com/expediator/trading-strategy-simulator](https://github.com/expediator/trading-strategy-simulator)

---

## Strategy: Golden Cross / Death Cross

- **Golden Cross** — 50-day SMA crosses **above** 200-day SMA → **BUY signal**
- **Death Cross** — 50-day SMA crosses **below** 200-day SMA → **SELL signal**

This is a well-known momentum strategy used by retail and institutional traders.

## What It Does

1. Downloads historical OHLCV data from Yahoo Finance for any stock ticker
2. Computes SMA-50 and SMA-200 rolling averages
3. Detects crossover points (buy/sell signals)
4. Simulates a portfolio starting from a configurable capital amount
5. Outputs:
   - Total return (%)
   - Number of trades
   - Win rate
   - Max drawdown
   - Matplotlib chart of price + SMAs + buy/sell markers

## Usage

```bash
pip install pandas yfinance matplotlib
python trading_sim.py
```

Edit the constants at the top of `trading_sim.py`:
```python
TICKER  = 'AAPL'     # any Yahoo Finance ticker
START   = '2018-01-01'
END     = '2024-01-01'
CAPITAL = 10000      # starting portfolio in USD
```

## Output

```
Ticker: AAPL | 2018-01-01 → 2024-01-01
Starting capital:  $10,000.00
Ending value:      $24,318.42
Total return:      143.18%
Trades executed:   8
Wins / Losses:     5 / 3
Max drawdown:      -18.4%
```

A Matplotlib window opens showing the price chart with SMA lines and buy/sell arrows.

## Files

```
trading-strategy-simulator/
├── trading_sim.py    ← Main script
└── README.md
```

## Limitations

- Past performance does not predict future results
- SMA strategies underperform in sideways/choppy markets
- No transaction costs, slippage, or taxes modelled
- For educational purposes only — not financial advice
