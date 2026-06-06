import numpy as np
from analysis.loader import load_stats
from analysis.cleaner import clean
from analysis.metrics import assist_to_turnover_ratio, simple_PER, per_36, assign_tiers, min_max_normalizer
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
PER_results = simple_PER(stats)
atr_results = assist_to_turnover_ratio(stats)
pts_per_36 = per_36(stats)[:,0]
ast_per_36 = per_36(stats)[:,1]
reb_per_36 = per_36(stats)[:,2]

output_arr = np.column_stack([
    PER_results, 
    atr_results,
    pts_per_36,
    ast_per_36,
    reb_per_36
    ])
print(output_arr)

np.save('output/player_metrics.npy',output_arr)
loaded_data = np.load('output/player_metrics.npy')

normalized_arr = np.column_stack([
    min_max_normalizer(PER_results),
    min_max_normalizer(atr_results),
    min_max_normalizer(pts_per_36),
    min_max_normalizer(ast_per_36),
    min_max_normalizer(reb_per_36)
    ])
print(normalized_arr)

np.save('output/normalized_metrics.npy',output_arr)
loaded_normalized_data = np.load('output/normalized_metrics.npy')

if output_arr.shape == loaded_data.shape and normalized_arr.shape == loaded_normalized_data.shape:
    print("-- Data Shape maintained after re-load --")
else: 
    print("-- Error in data save or inport --")

# ----- Correlation Matrix -----
#initialize matrix 
corr_matrix = np.zeros((8,8))

for i in range(8):
    for j in range(8):
        x = stats[:,i]
        y = stats[:,j]
        
        r = sum((x - np.mean(x)) * (y - np.mean(y))) / (len(names) * np.std(x) * np.std(y))
        corr_matrix[i,j] = r

print(" -- Correlation Matrix (Manual Calculation) --")
print(corr_matrix)

print(" -- Correlation Matrix (numPY Calculation) --")
print(np.corrcoef(stats.T))

if np.allclose(corr_matrix, np.corrcoef(stats.T)):
    print("Correlation matrices match")
else: 
    print("The matrices do not match, check your calculations")