# %load q02_confidence_interval/build.py
# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']
def confidence_interval(sample=sample):
    z=stats.norm.ppf(q=0.95)
    lower_limit_95CI=sample.mean()-(z*sample.std()/(sample.count()**.5))
    upper_limit_95CI=sample.mean()+(z*sample.std()/(sample.count()**.5))
    return lower_limit_95CI, upper_limit_95CI



