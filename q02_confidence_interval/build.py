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
    smean=sample.mean()
    ssize=sample.count()
    z_val=stats.norm.ppf(q=0.95)
    p_stdev=sample.std()
    margin=z_val*(p_stdev/math.sqrt(ssize))
    
    confidence_interval=(smean-margin,smean+margin)
    return confidence_interval
    #print(confidence_interval)
    
#confidence_interval(sample)


