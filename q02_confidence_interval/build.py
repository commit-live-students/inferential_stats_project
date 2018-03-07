# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']

# Write your solution here :
def confidence_interval(sample):
    mean = sample.mean()
    sd = sample.std()
    z_value = stats.norm.ppf(q = .95)
    lower_limit_of_confidence_interval = mean - z_value*(sd/math.sqrt(1460))
    high = mean + z_value*(sd/math.sqrt(1460))
    return lower_limit_of_confidence_interval, high

confidence_interval(sample)
