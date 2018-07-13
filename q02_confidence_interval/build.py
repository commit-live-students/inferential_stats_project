# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']
sample_mean = sample.mean()
sample_sd = sample.std()
z_critical = stats.norm.ppf(q = 0.95)
standard_error = sample_sd / math.sqrt(sample.count())
#print standard_error


# Write your solution here :
def confidence_interval(sample):
    estimate = z_critical * standard_error
    lower_ci = sample_mean - estimate
    upper_ci = sample_mean + estimate

    return lower_ci, upper_ci
print confidence_interval(sample)
