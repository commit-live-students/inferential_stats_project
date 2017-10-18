# Default imports
import math
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']
def confidence_interval(sample):
    sample_size = 1460
    sample_mean = sample.mean()
    z_critical = 1.64485362695
    sigma = sample.std()
    standard_error = sigma/math.sqrt(sample_size)
    Estimate = (z_critical)*(standard_error)
    lower_limit = sample_mean - Estimate
    upper_limit = sample_mean + Estimate
    return lower_limit,upper_limit

# Write your solution here :
