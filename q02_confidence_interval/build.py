# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']


# Write your solution here :
def confidence_interval(sample):
    mean = sample.mean()
    var = sample.var()
    stand_dev = np.sqrt(var)
    #print stand_dev

    stand_error = stand_dev/np.sqrt(sample.shape[0])
    #print stand_error

    z = stats.norm.ppf(0.95)
    low_conf_intrval = mean - z * stand_error
    #print(low_conf_intrval)
    up_conf_intrval = mean + z * stand_error
    #print(up_conf_intrval)
    return low_conf_intrval, up_conf_intrval

confidence_interval(sample)
