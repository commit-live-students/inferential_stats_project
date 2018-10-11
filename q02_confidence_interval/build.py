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
    sample_mean=sample.mean()
    sample_deviation=sample.std()
    size=len(sample.values)
    LCI=sample_mean-z_critical*(sample_deviation/(size**0.5))
    UCI=sample_mean+z_critical*(sample_deviation/(size**0.5))
    
    return LCI,UCI


