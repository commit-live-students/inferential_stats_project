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
    sigma = sample.std()
    n = sample.count()
    standard_error = sigma/math.sqrt(n)
    
    z_value = stats.norm.ppf(q = 0.95)
    
    estimate = z_value * standard_error

    lower_limit = sample.mean() - estimate
    upper_limit = sample.mean() + estimate
    return lower_limit, upper_limit



confidence_interval(sample)


