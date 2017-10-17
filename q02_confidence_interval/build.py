# Default imports
import math
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']


# Write your solution here :
def confidence_interval(sample):
    z_critical = 1.645#for 90% Confidence interval
    std_dev_sample = sample.std()

    margin_of_error = z_critical * (std_dev_sample / math.sqrt(len(sample)))
    interval = ((sample.mean() - margin_of_error), (sample.mean() + margin_of_error))
    return interval

confidence_interval(sample)
