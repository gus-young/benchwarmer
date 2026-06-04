from analysis.loader import load_stats
from analysis.cleaner import clean

names, stats = load_stats()
names, stats = clean(names, stats)
print(f"Clean dataset: {len(names)} players, {stats.shape[1]} features")