# %load q02_confidence_interval/build.py
# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']
def confidence_interval(sample) :
    stdErr=sample.std()/math.sqrt(sample.shape[0])
    
    z=stats.norm.ppf(q=0.95)
    marginError=z*stdErr
    confidence=(sample.mean()-marginError,sample.mean()+marginError)
    return(confidence)
#   
# Write your solution here :

#confidence_interval(sample)



