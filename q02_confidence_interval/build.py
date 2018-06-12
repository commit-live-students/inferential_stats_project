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

    size, _, mean, var, _, _ = stats.describe(sample)
    conf_int = stats.norm.interval(0.9, loc=mean, scale=math.sqrt(var/size))
    return conf_int
print (confidence_interval(sample))





