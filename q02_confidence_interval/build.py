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
    sample_mean=sample.mean()
    z_critical = stats.norm.ppf(q = 0.95)  # Get the z-critical value*
    sam_stdev = df['GrLivArea'].std()
    margin=z_critical*(sam_stdev/math.sqrt(df.GrLivArea.shape[0]))
    conf=(sample_mean - margin, sample_mean + margin)
    return conf
confidence_interval(sample)

