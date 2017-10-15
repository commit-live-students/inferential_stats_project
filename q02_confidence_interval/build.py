# %load q02_confidence_interval/build.py
# Default imports
import math
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']


def confidence_interval(sample):
    #sample = data['GrLivArea']
    mean = sample.mean()
    std = sample.std()
    n = len(sample)
#     print(sample.std())
    z= stats.norm.ppf(0.95)
    lower_limit = mean - z*(std/n**0.5)
    upper_limit = mean + z*(std/n**0.5)
    #     lower_limit =
    return (lower_limit,upper_limit)
