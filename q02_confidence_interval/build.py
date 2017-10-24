# %load q02_confidence_interval/build.py
# Default imports
import math
import numpy as np
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']


def confidence_interval(sample):

    np.random.seed(10)

    sample_size = 1000
    sample_mean = sample.mean()

    z_critical = stats.norm.ppf(q = 0.95)  # Get the z-critical value*

#     print("z-critical value:")              # Check the z-critical value
#     print(z_critical)

    pop_stdev = sample.std()  # Get the population standard deviation

    margin_of_error = z_critical * (pop_stdev/math.sqrt(len(sample)))

    confidence_interval = (sample_mean - margin_of_error,
                       sample_mean + margin_of_error)

    #print("Confidence interval:")
    return(confidence_interval)
    #print("True mean: {}".format(sample.mean()))

confidence_interval(sample)
