# BenchWarmer

A basketball player statistics analysis pipeline built with NumPy. Ingests raw player data, cleans it, computes advanced performance metrics, and generates ranked reports—all using core NumPy without Pandas or scikit-learn.

This project is intentionally **written by hand** and built from scratch to demonstrate NumPy fundamentals: boolean masking, broadcasting, vectorization, z-scores, normalization, and binary file I/O.

---

## Features

- **Data cleaning** — filters players below a minimum games threshold and imputes corrupted field goal percentage values
- **Advanced metrics** — computes Player Efficiency Rating (PER), assist-to-turnover ratio, and per-36-minute stats using broadcasting
- **Ranking and outlier detection** — ranks players using `np.argsort()` and flags statistical outliers via z-scores
- **Tier classification** — assigns players to Elite / Starter / Rotation / Bench tiers using percentile thresholds
- **Normalization** — scales each metric column to [0, 1] using min-max normalization
- **Correlation analysis** — manually computes a correlation matrix and validates it against `np.corrcoef()`
- **File I/O** — saves and reloads computed metrics as `.npy` binary files

---

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

---

## Requirements

- Python 3.x
- NumPy

Install NumPy if needed:

```bash
pip install numpy
```

---

## Usage

```bash
python main.py
```

The pipeline will:

1. Load raw player statistics from `data/players.py`
2. Clean the dataset (remove low-game-count players, fix zero field goal %)
3. Compute PER, assist-to-turnover ratio, and per-36-minute stats
4. Print top-5 leaderboards and any statistical outliers
5. Assign tier labels to every player
6. Save metrics to `output/player_metrics.npy` and `output/normalized_metrics.npy`
7. Compute and verify a correlation matrix across all metrics

### Example output

```
Clean dataset: 18 players, 8 features

--- Top 5 by PER ---
1. Jaylen Cross    — 42.30
2. Marcus Dillon   — 40.15
...

--- Outliers ---
1. Tyler Bosh        0.30

--- Tier Assignments ---
Elite:    Jaylen Cross, Marcus Dillon
Starter:  ...
```

---

## NumPy Concepts Covered

| Concept                   | Where used                                             |
| ------------------------- | ------------------------------------------------------ |
| Boolean masking           | `cleaner.py` — filtering players by games played       |
| Broadcasting              | `metrics.py` — per-36 computation across (n, 3) / (n,) |
| `np.argsort()`            | `reporter.py` — ranking players                        |
| `np.where()`              | `metrics.py` — nested tier assignment                  |
| Z-scores                  | `reporter.py` — outlier detection                      |
| Min-max normalization     | `metrics.py` — scaling metrics to [0, 1]               |
| `np.corrcoef()`           | `main.py` — correlation matrix validation              |
| `np.save()` / `np.load()` | `main.py` — binary file persistence                    |

---

## Data Notes

The raw dataset in `data/players.py` includes two intentional data quality issues to exercise the cleaning pipeline:

- **Two players** have fewer than 20 games played (injured; filtered out)
- **One player** has a field goal percentage of 0% (data corruption; imputed with the column mean)
