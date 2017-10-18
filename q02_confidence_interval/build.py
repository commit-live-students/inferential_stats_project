# %load q02_confidence_interval/build.py
# Default imports
import math
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']

def confidence_interval(sample):
    size = len(sample)
    samplemean = sample.mean()
    samplesd = sample.std()
    z_critical = stats.norm.ppf(q = 0.95)
    errormargin = z_critical * (samplesd/math.sqrt(size))

    #print(samplemean, samplesd, z_critical, size, errormargin)
    return (samplemean - errormargin), (samplemean + errormargin)
# Write your solution here :
confidence_interval(sample)
