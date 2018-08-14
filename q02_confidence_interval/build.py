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
    sample_mean = sample.mean()
    sample_std_dev = sample.std()

    z_critical = stats.norm.ppf(q = 0.95)  # Get the z-critical value*
    
    margin_of_error = z_critical * (sample_std_dev/math.sqrt(len(sample)))

    confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)
    low = confidence_interval[0]
    high = confidence_interval[1]

    return low, high 

confidence_interval(sample)

