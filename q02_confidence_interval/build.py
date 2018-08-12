# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']


# Write your solution here :
def confidence_interval(sample):
    sample_size=sample.shape[0]
    sample_mean=sample.mean()
    z_val = stats.norm.ppf(q = 0.95)
    stdev = sample.std()
    margin_of_error = z_val * (stdev/math.sqrt(sample_size))
    confidence_interval = (sample_mean - margin_of_error,sample_mean + margin_of_error)
    return confidence_interval[0],confidence_interval[1]
