# Default imports
import math
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']

def confidence_interval(sample):
    sample_size = sample.shape[0]
    sample_mean = sample.mean()
    z_critical = stats.norm.ppf(q=0.95)
    sample_sd = sample.std()
    margin_err = z_critical*(sample_sd/math.sqrt(sample_size))
    lower_limit = sample_mean - margin_err
    upper_limit = sample_mean + margin_err
    return lower_limit,upper_limit
