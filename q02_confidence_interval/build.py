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
    z_critical = stats.norm.ppf(q = 0.95)
    grlivarea_sd = sample.std()
    margin_of_error = z_critical * (grlivarea_sd/math.sqrt(sample.size))
    sample_mean = sample.mean()
    return (sample_mean - margin_of_error), (sample_mean + margin_of_error)
    
low, high = confidence_interval(sample)

