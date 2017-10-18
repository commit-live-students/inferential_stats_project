# Default imports
import math
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']


# Write your solution here :
def confidence_interval(sample):
    sample_size=len(sample)
    sample_mean = sample.mean()
    z_critical = stats.norm.ppf(q = 0.95)  # Get the z-critical value*
    stdev = sample.std()  # Get the population standard deviation
    margin_of_error = z_critical * (stdev/math.sqrt(sample_size))
    confidence_interval = (sample_mean - margin_of_error,
                           sample_mean + margin_of_error)
    return confidence_interval
