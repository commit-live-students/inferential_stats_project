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
    # print sample_mean
    z_critical = stats.norm.ppf(q = 0.95)  # Get the z-critical value*
    # print z_critical
    std_dev = sample.std()
    # print std_dev
    sample_size = len(sample.index)
    # print sample_size
    margin_of_error = z_critical * (std_dev/math.sqrt(sample_size))
    # print margin_of_error
    confidence_interval = (sample_mean - margin_of_error,
                           sample_mean + margin_of_error)
    return confidence_interval
