# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']


# Write your solution here :
def confidence_interval(sample):
    sample.replace(to_replace='',value='NA',inplace=True)
    me = sample.mean(skipna=True)
    std = sample.std(skipna=True)
    z = stats.norm.ppf(q = 0.95)
    n = sample.shape[0]
    se = std / float(math.sqrt(n))
    est = z * (se)
    max1 = me + est
    min1 = me - est
    return min1, max1
