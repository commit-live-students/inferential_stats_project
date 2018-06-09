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
    n = len(sample)
    sample_mean = sample.mean()
    sigma = sample.std()
    z_critical = stats.norm.ppf(q = 0.95)
    margin_of_error = z_critical * (sigma/math.sqrt(n))
    return sample_mean - margin_of_error, sample_mean + margin_of_error




