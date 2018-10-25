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
    '''Function that calculates the confidence 
        interval '''
    
    #calculate the statistics of sample
    z = stats.norm.ppf(q=0.95)
    mean = sample.mean()
    sigma = sample.std()
    n = sample.shape[0]
    
    #calculate the interval
    interval_upper = mean + z*(sigma/(n)**0.5)
    interval_lower = mean - z*(sigma/(n)**0.5)
    
    return interval_lower , interval_upper

#call the function 
confidence_interval(sample)





