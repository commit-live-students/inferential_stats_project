# Default imports
import math
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']

def confidence_interval(sample):
    sample_size=sample.shape[0]
    sample_mean = sample.mean()

    z_critical = stats.norm.ppf(q = 0.95)  # Get the z-critical value*
    sigma=sample.std()
    margin_of_error = z_critical * (sigma/math.sqrt(sample_size))

    confidence_interval = (sample_mean - margin_of_error,
                           sample_mean + margin_of_error)
    lower_limit=sample_mean - margin_of_error
    upper_limit=sample_mean + margin_of_error
    return lower_limit,upper_limit
# Write your solution here :
