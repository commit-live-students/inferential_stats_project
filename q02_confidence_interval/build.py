# %load q02_confidence_interval/build.py
# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']


# Write your solution here :

def confidence_interval(sample):
    std_dev=sample.std()
    n=sample.shape[0]
    mean=sample.mean()
    z_crtitical=stats.norm.ppf(q=0.95)
    margin_of_error=z_crtitical*(std_dev/math.sqrt(n))
    confidence_interval=(float(mean-margin_of_error)),float(mean+margin_of_error)
    return (confidence_interval)

confidence_interval(sample)

    




