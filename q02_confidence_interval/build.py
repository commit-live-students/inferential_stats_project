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
    sample_mean = sample.mean()

    z_critical = stats.norm.ppf(q = 0.95)  # Get the z-critical value*         
    sample_size = df['GrLivArea'].count()
    sample_stdev = sample.std()  # Get the sample standard deviation

    margin_of_error = z_critical * (sample_stdev/math.sqrt(sample_size))

    lower_limit = sample_mean - margin_of_error
    upper_limit = sample_mean + margin_of_error
    return lower_limit, upper_limit



