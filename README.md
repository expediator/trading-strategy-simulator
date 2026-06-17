# Trading Strategy Simulator

A Python script that backtests a classic **SMA crossover strategy** (50-day vs 200-day moving average) on real stock data from Yahoo Finance.

## Strategy

- **Buy** when SMA50 crosses above SMA200 (golden cross)
- **Sell** when SMA50 crosses below SMA200 (death cross)
- Simulates a portfolio starting at ₹1,00,00,000 (configurable)

## Usage

```bash
pip install pandas yfinance matplotlib
python trading_sim.py
```

Outputs:
- Initial and final portfolio value
- Plot of price vs SMA50 vs SMA200

## Customize

Edit the top of `trading_sim.py`:

```python
TICKER = "NVDA"          # stock symbol
START  = "2023-01-01"    # backtest start
END    = "2026-01-01"    # backtest end
CAPITAL = 10_000_000     # starting capital
```

## Stack

`Python` · `pandas` · `yfinance` · `matplotlib`
