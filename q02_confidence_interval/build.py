# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']

# Write your solution here :
def confidence_interval(sample):


    sample_mean=float(sample.mean())
    sample_size=sample.count()
    z=stats.norm.ppf(q=0.95)
    # print ("Z-Score :",z)

    sample_std=sample.std()

    estimate=float(z*(sample_std/math.sqrt(sample_size)))

    # print ("Margin of error :",estimate)
    low_limit=float((sample_mean)-estimate)
    up_limit=float((sample_mean)+estimate)

    # print ("Lower limit of confidence interval :",low_limit)
    # print ("Upper limit of confidence interval :",up_limit)
    return low_limit,up_limit

low,high = confidence_interval(sample)
print low,high
