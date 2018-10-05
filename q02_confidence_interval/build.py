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
    mean = sample.mean()
    deviation = sample.std()
    
    z_value = stats.norm.ppf(q = 0.95)
    std_error = z_value * (deviation/math.sqrt(len(sample)))
    confidence_interval = (mean - std_error, mean + std_error)
    return confidence_interval[0],confidence_interval[1]

print(confidence_interval(sample))


