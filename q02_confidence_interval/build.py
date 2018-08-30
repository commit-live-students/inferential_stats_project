# %load q02_confidence_interval/build.py
# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']


# Write your solution here :
def confidence_interval(sample):
    mean = sample.mean()
    z_crit = stats.norm.ppf(q=0.05)
    sample_std_deviation = sample.std()
    sample_std_error = sample_std_deviation/math.sqrt(sample.shape[0])
    upper_limit = mean - z_crit*sample_std_error
    lower_limit = mean + z_crit*sample_std_error
    return lower_limit,upper_limit
confidence_interval(sample)



