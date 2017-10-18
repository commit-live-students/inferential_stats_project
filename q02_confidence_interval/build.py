# Default imports
import math
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']


# Write your solution here :
def confidence_interval(sample):
    n = sample.shape[0]
    sigma = sample.mean()
    # z = 1.645
    z = stats.norm.ppf(q = 0.95)
    std_dev = sample.std()
    std_error = z*(std_dev/math.sqrt(n))
    return sigma-std_error,sigma+std_error
