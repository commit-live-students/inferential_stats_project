# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']


# Write your solution here :

def confidence_interval(sample):

    x_bar = sample.mean()
    s = sample.std()
    n = sample.count()
    z = stats.norm.ppf(q = 0.95)
    lower_limit = (x_bar-z*(s/math.sqrt(n)))
    upper_limit = (x_bar+z*(s/math.sqrt(n)))
    return lower_limit,upper_limit

print confidence_interval(sample)
