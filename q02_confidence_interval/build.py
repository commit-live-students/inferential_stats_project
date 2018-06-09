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
    sale_price = sample.loc[:'SalePrice']
    n = len(sale_price)
    sample_mean = sale_price.mean()
    z_critical = stats.norm.ppf(q = 0.95) 
    pop_stdev = sale_price.std()
    z_critical * (pop_stdev/math.sqrt(n))
    margin_error = z_critical * (pop_stdev/math.sqrt(n))
    interval1 = sample_mean - margin_error
    interval2 = sample_mean + margin_error
    return interval1, interval2
confidence_interval(sample)


