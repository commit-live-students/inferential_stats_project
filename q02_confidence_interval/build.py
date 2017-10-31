# Default imports
from __future__ import division
import math
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']


# Write your solution here :
def confidence_interval(sample):
    mean = sample.mean()
    z = stats.norm.ppf(q=0.95)
    std = sample.std()
    n = sample.shape[0]
    estimate = z * (std/math.sqrt(n))
    return ((mean - estimate), (mean + estimate))
