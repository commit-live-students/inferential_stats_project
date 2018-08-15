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
    a=sample.mean()
    b=sample.std()
    c=len(sample)
    stderror=b/math.sqrt(c)
    z_critical=stats.norm.ppf(q=0.95)
    estimate=z_critical*stderror
    lowerlimit=a-estimate
    upperlimit=a+estimate
    return lowerlimit,upperlimit
    
    
    
    



c=confidence_interval(sample)
c


