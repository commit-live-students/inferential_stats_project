# %load q02_confidence_interval/build.py
# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']

def confidence_interval(sample):
    
    n = sample.shape[0]

    std = df['GrLivArea'].std()

    mean = np.mean(sample)

    error = std/(math.sqrt(n))

    z_value = stats.norm.ppf(q = 0.95)

    estimate = z_value* error

    low = mean - estimate
    high = mean + estimate

    return low,high
    

confidence_interval(sample)



# Write your solution here :



