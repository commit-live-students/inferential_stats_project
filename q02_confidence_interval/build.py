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
    mean= sample.mean()
    std= sample.std()
    se= std/math.sqrt(sample.shape[0])
    z_critical = stats.norm.ppf(q = 0.95)
    margin_of_error = z_critical * (se)
    low=mean-margin_of_error
    high= mean+margin_of_error
    return low,high

confidence_interval(sample)


