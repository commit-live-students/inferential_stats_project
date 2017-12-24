# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']


# Write your solution here :
def confidence_interval(sample):
    m = sample.mean()
    se = stats.sem(sample)
    z_crit = stats.norm.ppf(q=0.95) # Calculated value
    estimate = z_crit * se
    return m-estimate, m+estimate

print confidence_interval(sample)
