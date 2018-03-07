
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample_data = df['GrLivArea']
print sample_data.shape
def confidence_interval(sample_data):
    np.random.seed(10)

    sample_size = 1460
    sample = np.random.choice(sample_data, size = sample_size) #Generate a random sample from a given data
    sample_mean = sample_data.mean() #Get the sample mean
    sigma = sample_data.std() #Get the sample standard deviation

    z_value = stats.norm.ppf(q = 0.95)  # Get the z-critical value*
    print("z_value:")
    print z_value

    margin_of_error = z_value * (sigma/math.sqrt(sample_size))

    confidence_interval = (sample_mean - margin_of_error,
                           sample_mean + margin_of_error)

    print("Confidence interval:")
    print(confidence_interval)
    print("True mean: {}".format(sample_data.mean()))
    return confidence_interval
print confidence_interval(sample_data)
