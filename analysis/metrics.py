import numpy as np

def assist_to_turnover_ratio(stats):
    assists = stats[:, 3]
    turnovers = stats[:, 6]
    with np.errstate(divide='ignore', invalid='ignore'):
        at_ratio = assists / turnovers

    #find and make array w/o nan or inf values 
    is_finite_check = np.isfinite(at_ratio)
    finite_list = at_ratio[is_finite_check]
    
    #find max value in finite list 
    max_value = np.max(finite_list) 

    #replace nan/inf with max finite value 
    test_array = ~np.isfinite(at_ratio)
    at_ratio[test_array] = max_value

    return (at_ratio)

def simple_PER(stats):
    return stats[:, 2] + stats[:, 3] + stats[:, 4] + stats[:,5] - stats[:, 6]

def per_36(stats):
    par = stats[:, 2:5]
    minutes = stats[:,1]

    result = (par / minutes[:, np.newaxis]) * 36
    return result

def min_max_normalizer(arr):
    max_value = np.max(arr)
    min_value = np.min(arr)

    if max_value == min_value: 
        return np.zeros(arr.shape)
    
    else: 
        return (arr - min_value) / (max_value - min_value)

def assign_tiers(metric_array):
    pct_list = [75, 50, 25]
    pct_value_list = []

    for pct in pct_list: 
        pct_value_list.append(np.percentile(metric_array, pct))
    
    mask_elite = metric_array > pct_value_list[0]
    mask_starter = (metric_array > pct_value_list[1]) & (metric_array <= pct_value_list[0])
    mask_rotation = (metric_array > pct_value_list[2]) & (metric_array <= pct_value_list[1])
    mask_bench = metric_array < pct_value_list[2]

    tier_list = np.where(mask_elite, "Elite", np.where(mask_starter, "Starter", np.where(mask_rotation, "Rotation", np.where(mask_bench, "Bench", "Unk"))))

    return tier_list