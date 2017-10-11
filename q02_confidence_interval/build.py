# %load q02_confidence_interval/build.py
# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']
print((sample.shape[0]))

# Write your solution here :

def confidence_interval(sample):
    noOfSample=sample.shape[0]
    meanOfSample=sample.mean()
    sigmaOfSample=sample.sum()
    #print(noOfSample)
    #print(meanOfSample)
    #print(sigmaOfSample)

    standardDeviation=sample.std()

    z = stats.norm.ppf(q = 0.95)  # Get the z-critical value*


    standardError=standardDeviation/math.sqrt(noOfSample)
    #print(standardError)

    #print(standardDeviation)


    #z= 1.96
    low=meanOfSample-(z*standardError)
    high=meanOfSample+(z*standardError)
    return low.item(),high.item()

#confidence_interval(sample)
