# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']


# Write your solution here :
def confidence_interval(sample):
    mean = sample.mean()
    pop_stdev = sample.std()
    n = len(sample)

    z_critical = stats.norm.ppf(.95)
    se = pop_stdev / math.sqrt(n)
    margin_of_error = z_critical * se

    lower = mean - margin_of_error
    upper = mean + margin_of_error

    return lower, upper
