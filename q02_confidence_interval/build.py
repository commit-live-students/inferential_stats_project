# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']


def confidence_interval(samples):
    x = samples.mean()
    z = stats.norm.ppf( q =0.95)
    n = len(samples)
    s = samples.std()
    margin_of_error = (z * s) / math.sqrt(n)
    confidence_interval = (x - margin_of_error , x + margin_of_error)
    return confidence_interval

confidence_interval(sample)
