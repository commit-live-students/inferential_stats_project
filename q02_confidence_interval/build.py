# %load q02_confidence_interval/build.py
# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']


def confidence_interval(sample):
    n = sample.shape[0]
    mean = sample.mean()
    sd = sample.std()/(math.sqrt(n))
    z_critical = stats.norm.ppf(q = 0.95)
    margin_error = z_critical * (sd)
    CI = mean-margin_error,mean+margin_error
    return CI
