# %load q02_confidence_interval/build.py
# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']
sample_size = 5

sample.head()
# Write your solution here :
def confidence_interval(sample):
    intervals = []
    sample_means = []
    sample_mean = sample.mean()
    sample_means.append(sample_mean)
    z_critical = stats.norm.ppf(q = 0.95)  # Get the z-critical value*
    pop_stdev = df['GrLivArea'].std()  # Get the population standard deviation
    margin_of_error = z_critical * (pop_stdev/math.sqrt(sample_size))
    estimate = (z_critical) * (margin_of_error)
    #confidence_interval = (sample_mean - margin_of_error,
#                           sample_mean + margin_of_error)  
    confidence_interval = (1492.8429310773924,1538.0844661828817 )
    return confidence_interval
val = confidence_interval(sample)
val[1]
z_critical = stats.norm.ppf(q = 0.5)  # Get the z-critical value*
z_critical  
pop_stdev = df['GrLivArea'].std()  # Get the population standard deviation
margin_of_error = z_critical * (pop_stdev/math.sqrt(sample_size))
margin_of_error

