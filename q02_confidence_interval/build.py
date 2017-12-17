# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']


# Write your solution here :
import scipy.stats as stats

def confidence_interval(sample):
    z_critical = stats.norm.ppf(q = 0.95)  # Get the z-critical valu
    sample_mean = sample.mean()
    sample_std = sample.std()
    sample_size = sample.size
    estimate_of_error = z_critical * (sample_std/math.sqrt(sample_size))
    lower_limit = sample_mean - estimate_of_error
    upper_limit = sample_mean + estimate_of_error
    return(lower_limit,upper_limit)

print confidence_interval(sample)
