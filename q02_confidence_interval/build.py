# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']

import scipy.stats as stats
import math
def confidence_interval(sample):
    sample_mean = sample.mean()
    z_val = stats.norm.ppf(q = 0.95)
    std_dev = sample.std()
    std_error = (std_dev/math.sqrt(len(sample)))
    estimate = z_val*std_error
    confidence_interval = (sample_mean - estimate,
                       sample_mean + estimate)

    print("Confidence interval:")
    print(confidence_interval)
    print("True mean: {}".format(sample.mean()))
    return (confidence_interval[0], confidence_interval[1])
