# Default imports
import math
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']

# Hint: when not using the population standard deviation, find confidence interval as:
#Estimate = (z-value) * (Standard Error)
#Standard Error = sigma/sqrt(n)

# Write your solution here :
def confidence_interval(sample_series):
    mean = sample_series.mean()
    pop_stdev = sample_series.std()
    n = len(sample_series)

    z_critical = stats.norm.ppf(.95)
    se = pop_stdev / math.sqrt(n)
    margin_of_error = z_critical * se

    lower = mean - margin_of_error
    upper = mean + margin_of_error

    return lower, upper


print confidence_interval(sample)
