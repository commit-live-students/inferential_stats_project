# %load q02_confidence_interval/build.py
# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']
def confidence_interval(sample=sample):
    z_critical = stats.norm.ppf(q = 0.95) 
    sample_size=sample.size
    sample_stdev = sample.std() 
    sample_mean=sample.mean()
    margin_of_error = z_critical * (sample_stdev/math.sqrt(sample_size))
    Lower_confidence_interval = (sample_mean - margin_of_error)
    Upper_confidence_interval = (sample_mean + margin_of_error)  
    return Lower_confidence_interval,Upper_confidence_interval
confidence_interval()


