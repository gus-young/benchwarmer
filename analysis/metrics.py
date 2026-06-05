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
