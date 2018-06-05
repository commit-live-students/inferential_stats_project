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
    n = sample.count()
    sample_mean = sample.mean()
    z_critical = stats.norm.ppf(q=0.95)
    sample_std  = sample.std()

    estimate = z_critical * (sample_std/math.sqrt(n))
    lower = float(sample_mean - estimate)
    upper = float(sample_mean + estimate)
    #print('Lower: ',lower)
    #print('Upper: ',upper)
    return lower,upper

confidence_interval(sample)

