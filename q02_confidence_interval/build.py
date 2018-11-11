# %load q02_confidence_interval/build.py
# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']              #Sampling Analysis on GrLivArea



# Write your solution here :
def confidence_interval(sample):
    
    N     = sample.shape[0]               #Length of sample
    x_bar = sample.mean()                 #Sample mean
    Z     = stats.norm.ppf(q = 0.95)      #Z-critical  
    S     = sample.std()                  #S - Sample standard deviation
    Margin_Of_Error = Z*(S/math.sqrt(N))  #estimate to be subtracted/added from mean

    Lower_limit = x_bar - Margin_Of_Error #Lower limit of confidence interval
    Upper_limit = x_bar + Margin_Of_Error #Upper limit of confidence interval
    
    print('N               : ',N)
    print('x_bar           : ',x_bar)
    print('Z               : ',Z)
    print('S               : ',S)
    print('Margin of error : ',Margin_Of_Error)
    print('Lower Limit     : ',Lower_limit)
    print('Upper Limit     : ',Upper_limit)
    
    return Lower_limit,Upper_limit

#Call to the function
confidence_interval(sample)




