# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']


# Write your solution here :
def confidence_interval(df):
    se = sample.std()/math.sqrt((sample.shape[0]))
    z = stats.norm.ppf(q = 0.95)
    estimate = z * se
    return sample.mean() - estimate, sample.mean() + estimate
