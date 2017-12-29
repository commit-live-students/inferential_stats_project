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
    sample_size=len(sample)
    sample_mean = sample.mean()
    z_critical = stats.norm.ppf(q = 0.95)  # Get the z-critical value*
    pop_stdev = df['GrLivArea'].std()  # Get the population standard deviation
    margin_of_error = z_critical * (pop_stdev/math.sqrt(sample_size))
    low = (sample_mean - margin_of_error)
    high =(sample_mean + margin_of_error)
    return low,high
