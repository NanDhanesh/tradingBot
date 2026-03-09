# SwingTrader

A Python-based stock trading simulator that uses a **Random Forest machine learning model** to generate daily Buy, Sell, or Hold recommendations — then executes them against a virtual portfolio with built-in risk management rules.

> **Disclaimer:** This is a simulation only and should not be used for real financial trading.

---

## How It Works

1. You enter a stock ticker (any NYSE or NASDAQ stock with sufficient history)
2. Historical price data is fetched automatically via `yfinance`
3. A Random Forest model is trained on the historical data
4. The model makes daily trading decisions for the **most recent 300 trading days**
5. Decisions are executed only if they pass a set of risk rules
6. At the end, performance charts are displayed

---

## Requirements

- Python 3.7+
- Internet connection (for live data via `yfinance`)

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Simulator

### Full interactive mode

```bash
python main.py
```

### Quick mode (no sleep delays between days)

```bash
python quick.py
```

---

## Interactive Setup

When you run the simulator, you will be prompted for:

1. **Tutorial** — opt in to see an explanation of the system and its rules
2. **Portfolio size** — enter a starting capital amount (minimum $5,000)
3. **Stock ticker** — e.g. `AAPL`, `TSLA`, `NVDA`, `MSFT`

The stock must have at least ~800 days of trading history. Newly listed or delisted stocks will be rejected with a prompt to enter a new ticker.

---

## Risk Management Rules

All trade recommendations are subject to the following rules. If any rule is not met, the order is skipped.

| Rule | Description |
|------|-------------|
| **Confidence** | Buy orders require ≥50% model confidence; Sell orders require ≥45% |
| **Max allocation** | A new position will not be opened if less than 35% of capital is unallocated |
| **Position affordability** | A new position will not be opened if it costs more than available unallocated capital |
| **Minimum positions** | A sell will not be executed if there are no open positions |
| **Profit target** | A position is automatically sold if it rises **10%** from its buy price |
| **Stop loss** | A position is automatically sold if it falls **5%** from its buy price |
| **Lifespan** | A position is automatically sold after **10 trading days** if neither target nor stop has been hit |

**Position sizing:** Each new position is sized at **30% of current total account value**, divided by the current share price.

---

## Output

During the simulation, each trading day prints:

- The date
- Any positions hit by stop loss, profit target, or lifespan
- The recommendation (Buy / Hold / Sell) and whether it was executed
- Current account value, allocated capital, unallocated capital, and closed P&L

Color coding in the terminal:
- **Purple** — new position bought
- **Cyan** — position sold (manually)
- **Green** — profit target hit / profitable trade
- **Red** — stop loss hit / losing trade
- **Yellow** — lifespan exit

At the end of the 300-day simulation, two charts are displayed:
- **Left:** Total account capital over time
- **Right:** Stock price with buy (green) and sell (red) markers

---

## Pre-Optimised Tickers

The following tickers have a custom-tuned feature set for improved model performance:

| Ticker | Company |
|--------|---------|
| `AAPL` | Apple Inc. |
| `SPY` | S&P 500 ETF |
| `META` | Meta Platforms |
| `WMT` | Walmart |
| `SBUX` | Starbucks |

All other tickers use a general-purpose feature set.

---

## Project Structure

| File | Description |
|------|-------------|
| `main.py` | Main simulation loop |
| `quick.py` | Same as main but with sleep delays removed |
| `parameters.py` | Configuration values |
| `welcome_function.py` | Startup prompts and input validation |
| `tutorial_function.py` | In-app tutorial text |
| `data_formatting.py` | Fetches data via `yfinance` and engineers features |
| `feature_set_derival.py` | Selects the optimum feature set per ticker |
| `classifier_function.py` | Trains the Random Forest model and generates recommendations |
| `rule_creation.py` | Defines and checks all trading rules |
| `rule_class.py` | General rule class |
| `buy_rule_class.py` | Buy/Sell rule class |
| `portfolio_class.py` | Portfolio management (capital tracking, opening/closing positions) |
| `position_class.py` | Individual position with stop, target, and lifespan logic |
| `end_sim_function.py` | Closes all open positions and summarises results |
| `post_sim.py` | Generates performance charts |
| `typing_function.py` | Animated text output utility |
