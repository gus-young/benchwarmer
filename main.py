from analysis.loader import load_stats
from analysis.cleaner import clean
from analysis.metrics import assist_to_turnover_ratio, simple_PER, per_36

names, stats = load_stats()
names, stats = clean(names, stats)
print(f"Clean dataset: {len(names)} players, {stats.shape[1]} features")
print(per_36(stats))