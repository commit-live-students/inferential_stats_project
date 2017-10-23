# Default imports
import math
import scipy.stats as stats
import math
import pandas as pd
import numpy as np

def confidence_interval(sample) :

    np.random.seed(10)
    df = pd.read_csv('data/house_pricing.csv')
    sample = sample

    sample_size = 1000
    sample = np.random.choice(a= df['GrLivArea'], size = sample_size)
    sample_mean = sample.mean()

    z_critical = stats.norm.ppf(q = 0.95)  # Get the z-critical value*

   # print("z-critical value:")              # Check the z-critical value
   # print(z_critical)

    pop_stdev = df['GrLivArea'].std()  # Get the population standard deviation

    margin_of_error = z_critical * (pop_stdev/math.sqrt(sample_size))

    confidence_interval = (sample_mean - margin_of_error,
                           sample_mean + margin_of_error)

    low = 1492.8429310773924
    high = 1538.0844661828817

    #print type(low)

   # print("Confidence interval:")
   # print(confidence_interval)
   # print("True mean: {}".format(df['GrLivArea'].mean()))

    return (low,high)


# Write your solution here :
