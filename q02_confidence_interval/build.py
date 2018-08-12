# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']


# Write your solution here :
def confidence_interval(sample):
    samp_mean = sample.mean()
    samp_pop_stdev = sample.std()
    samp_n = len(sample)

    z_critical = stats.norm.ppf(.95)
    se = samp_pop_stdev / math.sqrt(samp_n)
    margin_of_error = z_critical * se

    samp_lower = samp_mean - margin_of_error
    samp_upper = samp_mean + margin_of_error

    return samp_lower, samp_upper
