# %load q02_confidence_interval/build.py
# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')

sample = df['GrLivArea']

def confidence_interval(sample):
    sample_size=sample.shape[0]

    # Write your solution here :
    #df confidence_interval(sample):

    #np.random.seed(10)

    #sample_size = 1000
    #sample = np.random.choice(a= data['SalePrice'], size = sample_size)
    sample_mean = sample.mean()

    z_critical = stats.norm.ppf(q = 0.95)  # Get the z-critical value*

    #print("z-critical value:")              # Check the z-critical value
    #print(z_critical)

    #pop_stdev = df['GrLivArea'].std()  # Get the population standard deviation
    sigma=sample.std()
    margin_of_error = z_critical * (sigma/math.sqrt(sample_size))

    confidence_interval = (sample_mean - margin_of_error,
                           sample_mean + margin_of_error)
    lower_limit=sample_mean - margin_of_error
    upper_limit=sample_mean + margin_of_error
    #print("Confidence interval:")
    #print(confidence_interval)
    #print("True mean: {}".format(df['GrLivArea'].mean()))
    return lower_limit,upper_limit

#l,h=confidence_interval(sample)
#print(l)
#print(h)
