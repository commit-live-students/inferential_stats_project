# Write your solution here :
# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
from math import sqrt

df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']
# Write your solution here :
def confidence_interval(sample):
    sample_mean = sample.mean()

    z_critical = stats.norm.ppf(q = 0.95)  # Get the z-critical value*

    #std = sqrt(sample.var())
    pop_stdev = sample.std()

    margin_of_error = z_critical * (pop_stdev/math.sqrt(len(sample)))
    confidence_interval = (sample_mean - margin_of_error,
                           sample_mean + margin_of_error)

    return confidence_interval[0],confidence_interval[1]
