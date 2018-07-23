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
    std = sample.std()
    print(mean)
    print(std)
    print(sample.shape[0])
    z_critical = stats.norm.ppf(q = 0.95)
    print(z_critical)
    errorMargin = std / math.sqrt(sample.shape[0])
    print(errorMargin)
    stdError = errorMargin * z_critical
    print(stdError)
    return [mean - stdError , mean + stdError]
    
confidence_interval(sample)
    




