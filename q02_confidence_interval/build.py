# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']


# Write your solution here :
def confidence_interval(sample):
    sigma = sample.std()
    standard_error = sigma/np.sqrt(sample.shape[0])
    mean = sample.mean()
    z_critical = stats.norm.ppf(0.95)
    lower_lim = mean - z_critical*standard_error
    upper_lim = mean + z_critical*standard_error
    return lower_lim,upper_lim
