#loads data from players.py
from data.players import RAW_STATS, PLAYER_NAMES
import numpy as np

def load_stats():
    stats_array = np.array(RAW_STATS, dtype=np.float64)
    return (PLAYER_NAMES, stats_array)
