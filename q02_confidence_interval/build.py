# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']


# Write your solution here :
def confidence_interval(sample1):
    sample_mean = sample1.mean()
    z_critical = stats.norm.ppf(q = 0.95)
    pop_stdev =  sample1.std()
    margin_of_error = z_critical * (pop_stdev/math.sqrt(len(sample1)))
    confidence_interval = (sample_mean - margin_of_error,
                       sample_mean + margin_of_error)
    return confidence_interval
