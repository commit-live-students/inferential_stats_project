# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']
def confidence_interval(sample):
    mean = sample.mean()
    var = sample.var()
    std_error = math.sqrt(var)/math.sqrt(sample.shape[0])
    critical = stats.norm.ppf(0.95)
    low = mean - critical*std_error
    high = mean + critical*std_error
    return low,high

# Write your solution here :
