<div align="center">

# 📈 Trading Strategy Simulator

**SMA 50/200 golden-cross backtester on real Yahoo Finance data**

[![GitHub](https://img.shields.io/badge/GitHub-expediator%2Ftrading--strategy--simulator-181717?style=flat-square&logo=github)](https://github.com/expediator/trading-strategy-simulator)
[![Python](https://img.shields.io/badge/Python_3.12-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square)](https://matplotlib.org)
[![yfinance](https://img.shields.io/badge/yfinance-239120?style=flat-square)](https://pypi.org/project/yfinance/)

Backtests a classic SMA golden-cross strategy on any stock ticker and outputs a full P&L report + price chart.

</div>

---

## Strategy

| Signal | Condition | Action |
|--------|-----------|--------|
| Golden Cross | SMA-50 crosses **above** SMA-200 | BUY |
| Death Cross | SMA-50 crosses **below** SMA-200 | SELL |

## Quick Start

```bash
pip install pandas yfinance matplotlib
python trading_sim.py
```

Edit constants at the top of `trading_sim.py`:

```python
TICKER  = 'AAPL'        # any Yahoo Finance ticker
START   = '2018-01-01'
END     = '2024-01-01'
CAPITAL = 10000
```

## Sample Output

```
Ticker: AAPL | 2018-01-01 → 2024-01-01
Starting capital:  $10,000.00
Ending value:      $24,318.42
Total return:      143.18%
Trades executed:   8
Wins / Losses:     5 / 3
Max drawdown:      -18.4%
```

A Matplotlib window opens with price chart, SMA-50, SMA-200, and buy/sell arrows.

## Files

```
trading-strategy-simulator/
├── trading_sim.py    ← Main script
└── README.md
```

> **Disclaimer:** Past performance does not predict future results. No transaction costs or slippage modelled. Not financial advice.

---

<div align="center">
An <strong>Expediator Inc.</strong> project · © 2026 · <a href="https://expediator.github.io/resume/">Portfolio</a>
</div>