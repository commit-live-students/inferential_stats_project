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
    sample_size = 1460
    sample_mean = sample.mean()
    z_critical = stats.norm.ppf(q = 0.95)
    stan_dev = sample.std()
    estimate = z_critical * (stan_dev/math.sqrt(sample_size))
    conf_inter = (sample_mean - estimate,
                       sample_mean + estimate)
    return conf_inter
confidence_interval(sample)

