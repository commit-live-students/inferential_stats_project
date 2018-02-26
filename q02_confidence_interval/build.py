# Default imports
from __future__ import division
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']
def confidence_interval(sample):
    n = sample.count()
    mean_value = sample.mean()
    sigma = sample.std()
    std_error = sigma/math.sqrt(n)
    z_critical = stats.norm.ppf(q = 0.95)
    estimate = z_critical*std_error
    confidence_interval = (mean_value - estimate,
                       mean_value + estimate)
    return confidence_interval



# Write your solution here :
