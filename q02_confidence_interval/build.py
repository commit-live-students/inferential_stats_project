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
    sample_size= sample.size
    pop_mean=sample.mean()
    z_critical = stats.norm.ppf(q = 0.95)  # Get the z-critical value*

#     print('z-critical value:')              # Check the z-critical value
#     print(z_critical)                        

    pop_stdev = sample.std()  # Get the population standard deviation

    margin_of_error = z_critical * (pop_stdev/math.sqrt(sample_size))

    lower_limit = pop_mean - margin_of_error
    upper_limit = pop_mean + margin_of_error
    return float(lower_limit),float(upper_limit)
confidence_interval(sample)




