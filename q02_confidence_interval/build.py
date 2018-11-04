# %load q02_confidence_interval/build.py
# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']
#print(sample)

# Write your solution here :
def confidence_interval(df):
    mean = np.mean(sample)
    print('mean=', mean)
    stand_error = stats.sem(sample)
    print('std_err=',stand_error)
    z_value = stats.norm.ppf(0.95)
    print('z value=', z_value)
    low_val = mean - (z_value * stand_error)
    up_val = mean + (z_value*stand_error)
    return low_val,up_val
    
confidence_interval(df)




