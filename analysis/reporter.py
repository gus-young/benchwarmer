import numpy as np

def top_n(names, metric_array, n=5, label="Metric"):
    descending_arr = np.argsort(metric_array)[::-1]
    leaderboard_list = descending_arr[:n]
    sorted_names = [names[i] for i in leaderboard_list]
    sorted_metric = metric_array[leaderboard_list]
    
    print(f"--- Top {n} by {label} ---")

    for index, (name, metric) in enumerate(zip(sorted_names, sorted_metric)):
        print(f"{index+1}. {name}        {metric}")

def find_outliers(names, metric_array, label="Metric", threshold=2.0):
    arr_mean = np.mean(metric_array)
    arr_stdev = np.std(metric_array)
    z_score = np.abs(metric_array - arr_mean) / arr_stdev
    z_mask = z_score > threshold

    outlier_stats = metric_array[z_mask]
    name_index = np.where(z_mask)[0]
    outlier_names = [names[index] for index in name_index]

    print(f"--- {label} ---")
    
    for index, (name, metric) in enumerate(zip(outlier_names, outlier_stats)):
        print(f"{index+1}. {name}        {metric}")