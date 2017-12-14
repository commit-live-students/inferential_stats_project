# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']

def confidence_interval(sample):
    z_critical = stats.norm.ppf(q = 0.95)
    sample_mean = sample.mean()# Get the z-critical value*
    sample_size=sample.count()

    pop_stdev = sample.std()  # Get the population standard deviation

    margin_of_error = z_critical * (pop_stdev/math.sqrt(sample_size))

    confidence_interval = (sample_mean - margin_of_error,
                           sample_mean + margin_of_error)
    return sample_mean - margin_of_error,sample_mean + margin_of_error
# Write your solution here :
