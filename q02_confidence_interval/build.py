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
    z_value= stats.norm.ppf(q = 0.95)                       
    estimate= z_value* (df['GrLivArea'].std()/math.sqrt(sample.shape[0]))
    confidence_interval = sample_mean - estimate,sample_mean + estimate
    return confidence_interval






