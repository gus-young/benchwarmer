# BenchWarmer

A basketball player statistics analysis pipeline built with NumPy. Ingests raw player data, cleans it, computes advanced performance metrics, and generates ranked reports—all using core NumPy without Pandas or scikit-learn.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python) ![NumPy](https://img.shields.io/badge/NumPy-1.x-green?logo=numpy)

## Features

- Data cleaning that filters players below a minimum games threshold and imputes corrupted field goal percentage values
- Advanced metrics — PER, assist-to-turnover ratio, and per-36-minute stats computed with broadcasting
- Player ranking via `np.argsort()` and statistical outlier detection via z-scores
- Tier classification assigning players to Elite / Starter / Rotation / Bench using percentile thresholds
- Min-max normalization scaling each metric column to [0, 1]
- Correlation matrix computed manually and validated against `np.corrcoef()`
- Binary file I/O saving and reloading computed metrics as `.npy` files

## Getting Started

**Requirements:** Python 3.x, NumPy

```bash
git clone https://github.com/gus-young/benchwarmer.git
cd benchwarmer
pip install numpy
python main.py
```

## Project Structure

```
benchwarmer/
├── main.py                   # Pipeline entry point
├── data/
│   └── players.py            # Raw player stats (20 fictional players, intentional data issues)
├── analysis/
│   ├── loader.py             # Converts raw data to NumPy array
│   ├── cleaner.py            # Filters and imputes data quality issues
│   ├── metrics.py            # Computes PER, ATR, per-36, normalization, tier assignment
│   └── reporter.py           # Prints leaderboards and outlier reports
└── output/
    ├── player_metrics.npy    # Saved computed metrics (generated at runtime)
    └── normalized_metrics.npy
```
