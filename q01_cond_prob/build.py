# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')
data = pd.DataFrame(df)

# Enter Code Here
def cond_prob(df):
    result = data.shape[0]
    ho = data[data['Neighborhood'] == 'OldTown'].shape[0]
    cp = float((ho/result)*((ho - 1)/(result - 1))*((ho - 2)/(result - 2)))
    return cp
cond_prob(df)




