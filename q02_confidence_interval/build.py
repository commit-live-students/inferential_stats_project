# Default imports
import scipy.stats
import scipy
import pandas as pd
import numpy as np
import math

df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']

def confidence_interval(sample_series):
    mean = sample_series.mean()
    stddev = sample_series.std()
    n = len(sample_series)
    z_critic = scipy.stats.norm.ppf(q=0.95)
    se = stddev/ math.sqrt(n)
    margin_of_err = z_critic * se
    lower = mean - margin_of_err
    upper = mean + margin_of_err
    return lower, upper
