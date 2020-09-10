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
    sigma = sample.std()
    z_value = stats.norm.ppf(.95)
    n = len(sample)

    std_err = sigma/np.sqrt(n)
    estimate = z_value * std_err

    upper = mean + estimate
    lower = mean - estimate
    return lower, upper



