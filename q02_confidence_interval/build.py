import math
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']
z_critical = stats.norm.ppf(q = 0.95)

def confidence_interval(sample):
    sample_mean = sample.mean()
    samplestd = sample.std()
    n = np.size(sample)
    stderror = samplestd/(n**(1/2))
    marginerror = z_critical*stderror
    lower = sample_mean - marginerror
    upper = sample_mean + marginerror
    
    return lower, upper

confidence_interval(sample)










