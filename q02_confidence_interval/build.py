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
    standard_dev=(sample.std())
    sample_size=(sample.count())
    z_critical = stats.norm.ppf(q = 0.95)
    standard_error=(standard_dev)/(math.sqrt(sample_size))
    estimate = z_critical*standard_error
    confidence_interval_p=np.mean(sample)+estimate
    confidence_interval_n=np.mean(sample)-estimate
    return (confidence_interval_n,confidence_interval_p)




