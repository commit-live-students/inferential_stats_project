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
#     std_err = sigma/sqrt(n)
#     estimate = (z_value) * (std_err)
    z_critical = stats.norm.ppf(q = 0.95)
    sample_mean = sample.mean()
    pop_stdev = sample.std()
    sample_size = sample.shape[0]
    margin_of_error = z_critical * (pop_stdev/math.sqrt(sample_size))
    confidence_interval = (sample_mean - margin_of_error,
                       sample_mean + margin_of_error)  
    return confidence_interval 








