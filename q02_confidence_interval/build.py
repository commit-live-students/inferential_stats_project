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
    mean = np.mean(sample)
    stand_error = stats.sem(sample)
    #print(stand_error)
    z_value = stats.norm.ppf(0.95)
    low_val = mean - (z_value * stand_error)
    up_val = mean + (z_value*stand_error)
    return low_val,up_val









