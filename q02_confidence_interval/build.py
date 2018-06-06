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
    standard_dev=(sample.std())
    sample_size=(sample.count())
    
    standard_error=(standard_dev)/(math.sqrt(sample_size))
    
    z = stats.norm.ppf(q = 0.95)
    
    estimate=z*standard_error
    
    ci_p=np.mean(sample)+estimate
    ci_n=np.mean(sample)-estimate
    return (ci_n,ci_p)



