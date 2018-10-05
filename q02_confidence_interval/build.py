# %load q02_confidence_interval/build.py
# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']

# def confidence_interval(sample, confidence=0.95):
#     a = 1.0 * np.array(sample)
#     n = len(a)
#     m, se = np.mean(a), scipy.stats.sem(a)
#     h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
#     return m, m-h, m+h
    
    
    



def confidence_interval(sample):
    mean = sample.mean()
    deviation = sample.std()
    
    z_value = stats.norm.ppf(q = 0.95)
    std_error = z_value * (deviation/math.sqrt(len(sample)))
    confidence_interval = (mean - std_error, mean + std_error)
    return confidence_interval[0],confidence_interval[1]
print(confidence_interval(sample))


