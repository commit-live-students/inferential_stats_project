# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']

def confidence_interval(sample):

    sample_size = sample.shape[0]
    sample_mean = sample.mean()

    # Get the z-critical value
    z_critical = stats.norm.ppf(q = 0.95)

    # Get the sample standard deviation
    sample_stdev = sample.std()

    # Standard error for the sample
    std_error = sample_stdev / math.sqrt(sample_size)

    # Margin of error for the sample
    margin_of_error = z_critical * std_error

    # Calculate confidence interval
    confidence_interval = (sample_mean - margin_of_error,
                       sample_mean + margin_of_error)

    return confidence_interval[0], confidence_interval[1]
