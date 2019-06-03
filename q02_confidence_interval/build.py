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
#    return stats.norm.interval(0.95, loc=sample.mean(), scale=sample.std()/np.sqrt(sample.shape[0]))
    z_score = stats.norm.ppf(q = 0.95)
    mean = sample.mean()
    std_err = sample.std()/math.sqrt(sample.size)
    margin_of_error = z_score * std_err
    return mean-margin_of_error ,mean+margin_of_error
confidence_interval(sample)

