# %load q02_confidence_interval/build.py
# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']


def confidence_interval(n):
    n = sample.size
    sample_mean = sample.mean()

    z_critical = stats.norm.ppf(q = 0.95)  # Get the z-critical value*

    print('z-critical value:')              # Check the z-critical value
    print(z_critical)                        

    Std_Error = (sample.std())/math.sqrt(n)

    est = (z_critical) * (Std_Error)

    conf_interval = (sample_mean - est,
                           sample_mean + est)
    return conf_interval
confidence_interval(sample)
sample.size



