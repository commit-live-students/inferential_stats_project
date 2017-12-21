# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']

z = stats.norm.ppf(q = 0.95)
def confidence_interval(sample):
    total = sample.shape[0]

    cal_mean = sample.mean()
    cal_std = sample.std()
    margin_of_error = z * (cal_std/math.sqrt(total))
    lower_limit_of_confidence_interval = cal_mean - margin_of_error
    upper_limit_of_confidence_interval = cal_mean + margin_of_error

    return (lower_limit_of_confidence_interval, upper_limit_of_confidence_interval)
