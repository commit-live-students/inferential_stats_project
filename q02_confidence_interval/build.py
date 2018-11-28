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
    mean = sample.mean()
    standard_error = sigma/np.sqrt(sample.shape[0])
    z_critical = stats.norm.ppf(0.95)
    interval_lower = mean - z_critical*standard_error
    interval_upper = mean + z_critical*standard_error
    return interval_lower,interval_upper
confidence_interval(sample)





