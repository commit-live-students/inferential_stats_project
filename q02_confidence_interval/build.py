#*SE %load q02_confidence_interval/build.py
# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']


# Write your solution here :

def confidence_interval(sample):
    SE = sample.std()/(len(sample)**.5)
    ll = sample.mean()- 1.644853626951477*SE
    ul = sample.mean()+ 1.644853626951477*SE
    return ll,ul


SE = sample.std()/(len(sample)**.5)
(1538.0844661828817-sample.mean())/SE


