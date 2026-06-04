import numpy as np

def filter_min_games(names, stats, min_games=20):
    #apply mask to column index 0 (games played) of the stats array
    mask = stats[:,0] >= min_games
    
    #create new array with filtered player stats removed
    filtered_stats = stats[mask]  

    #find indexes where the mas returned true
    name_index = np.where(mask)[0]

    #use the name_index to construct new list of player names 
    filtered_names = [names[index] for index in name_index]

    return (filtered_names, filtered_stats)

def fix_zero_fg_pct(stats):
    zero_fg_pct_mask = stats[:,7] == 0
    non_zero_fg_pct_mask = stats[:,7] != 0.0
    non_zero_fg_stats = stats[non_zero_fg_pct_mask]
    fg_pct = non_zero_fg_stats[:,7]
    avg_fg_pct = np.mean(fg_pct)
    stats[zero_fg_pct_mask, 7] = avg_fg_pct
    return (stats)

def clean(names, stats):
    updated_names, updated_stats = filter_min_games(names, stats)
    updated_stats = fix_zero_fg_pct(updated_stats)
    return(updated_names, updated_stats)