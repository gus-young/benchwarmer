import numpy as np
from analysis.loader import load_stats
from analysis.cleaner import filter_min_games, fix_zero_fg_pct, clean

names, stats = load_stats()
names, stats = clean(names, stats)
print(f"Clean dataset: {len(names)} players, {stats.shape[1]} features")