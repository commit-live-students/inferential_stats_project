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
    std = (stats.norm.ppf(0.950058) * np.std(sample)) / math.sqrt(sample.size)
    mean = np.mean(sample)
    return (mean-std, mean+std)


