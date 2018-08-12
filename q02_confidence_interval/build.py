# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']

def confidence_interval(sample):
    sampleSize = sample.shape[0]
    sampleMean = sample.mean()
    sampleSD = sample.std()
    zVal = stats.norm.ppf(q=0.95)
    stdErr = (sampleSD/math.sqrt(sampleSize))
    estimate = zVal*stdErr
    confidence_interval = (sampleMean - estimate, sampleMean + estimate)
    return confidence_interval
