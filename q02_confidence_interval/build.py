# %load q02_confidence_interval/build.py
# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']


# Write your solution here :
def confidence_interval(sampleData):
    sample_mean = sampleData.mean()
    sample_size = sampleData.shape[0]
    #print('Sample Size')
    #print(sample_size)
    z_critical = stats.norm.ppf(q = 0.95)  # Get the z-critical value*
    #print('z-critical value:')              # Check the z-critical value
    #print(z_critical)                        
    sample_stdev = df['GrLivArea'].std()  # Get the population standard deviation
    margin_of_error = z_critical * (sample_stdev/math.sqrt(sample_size))
    confidence_interval = (sample_mean - margin_of_error,
                       sample_mean + margin_of_error)  
    #print('Confidence interval:')
    #print(confidence_interval)
    #print(('True mean: {}'.format(df['GrLivArea'].mean())))
    return confidence_interval
    




