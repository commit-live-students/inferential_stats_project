# %load q02_confidence_interval/build.py
# Default imports
import math
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']

def confidence_interval(sample):
    z_critical = stats.norm.ppf(q = 0.95)
    sample_stdev = sample.std()
    stderr = sample_stdev/ math.sqrt(sample.shape[0])
    Estimate = z_critical * stderr
    lower = (sample.mean() - Estimate).astype(float)
    higher = (sample.mean() + Estimate).astype(float)
    return lower , higher


# Write your solution here :
