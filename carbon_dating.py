import math

T_HALF = 5730
DECAY_CONSTANT = -math.log(2)

def get_age_carbon_14_dating(carbon_14_ratio):
    """Returns the estimated age of the sample in year.
    carbon_14_ratio: the percent (0 < percent < 1) of carbon-14
    in the sample compared to the amount in living
    tissue (unitless).
    
    Raises:
        ValueError: If carbon_14_ratio is <= 0 or > 1.0
    """
    # Validate input - handle edge cases
    if carbon_14_ratio <= 0:
        raise ValueError("Carbon-14 ratio must be positive (greater than 0)")
    
    if carbon_14_ratio > 1.0:
        raise ValueError("Carbon-14 ratio cannot exceed 1.0 (sample cannot have more C-14 than living tissue)")
    
    return math.log(carbon_14_ratio) / DECAY_CONSTANT * T_HALF