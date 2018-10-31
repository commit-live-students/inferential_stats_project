# %load q02_confidence_interval/build.py
# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']


# Write your solution here :
def confidence_interval(df):
    
    sample_mean= sample.mean() #find the mean of sample
    z_critical = stats.norm.ppf(0.95)  # z-value
    sample_dev = sample.std() # stardard deviation of sample
    standard_error = z_critical * (sample_dev/(len(sample))**0.5) #standa
    lower_limit = sample_mean - standard_error
    upper_limit = sample_mean + standard_error
    
    return lower_limit, upper_limit



confidence_interval(df)


