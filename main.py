import numpy as np
from analysis.loader import load_stats
from analysis.cleaner import clean
from analysis.metrics import assist_to_turnover_ratio, simple_PER, per_36, assign_tiers
from analysis.reporter import top_n, find_outliers

names, stats = load_stats()
names, stats = clean(names, stats)

#dataset summary 
print(f"Clean dataset: {len(names)} players, {stats.shape[1]} features")

#Top 5 players by Simple PER
top_n(names, simple_PER(stats), label="PER")

#Top 5 players by Assist-to-Turnover ratio
top_n(names, assist_to_turnover_ratio(stats), label="ATR")

#Top 5 players by Points Per 36 Minutes
top_n(names, per_36(stats)[:,0], label = "Pts Per 36")

#Any outliers in PER (players more than 2 standard deviations away)
find_outliers(names, simple_PER(stats), label="Outliers")

#Tier assignments printed for all players
print("-- Player Tier Assignments --")
for index, (player_name, tier) in enumerate(zip(names, assign_tiers(simple_PER(stats)))):
    print(f"{index+1}. {player_name}: {tier}")

#stack metrics into single 2D array 
per_36_result = per_36(stats)
output_arr = np.column_stack([
    simple_PER(stats), 
    assist_to_turnover_ratio(stats),
    per_36_result[:,0],
    per_36_result[:,1],
    per_36_result[:,2],
    ])

np.save('output/player_metrics.npy',output_arr)
loaded_data = np.load('output/player_metrics.npy')

if output_arr.shape == loaded_data.shape:
    print("-- Data Shape maintained after re-load --")
else: 
    print("-- Error in data save or inport --")