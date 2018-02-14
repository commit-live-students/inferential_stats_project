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
    sample_size = sample.shape[0]

    z_critical = stats.norm.ppf(q = 0.95)

    pop_stdev = sample.std()

    margin_of_error = z_critical * (pop_stdev/math.sqrt(sample_size))

    confidence_interval_lower = float(sample_mean - margin_of_error)
    confidence_interval_upper = float(sample_mean + margin_of_error)
    return confidence_interval_lower, confidence_interval_upper
