# Default imports
import math
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']


# Write your solution here :
def confidence_interval(sample):
    size, _, mean, var, _, _ = stats.describe(sample)
    return stats.norm.interval(0.9, loc=mean, scale=math.sqrt(var / size))
