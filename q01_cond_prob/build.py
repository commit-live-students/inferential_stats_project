# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

#1460 oldtown houses
#113 oldtown
# Enter Code Here
#df[df.Neighborhood == 'OldTown'].shape
def cond_prob(df):
    conditional_prob = 113/1460 * 112/1459 * 111/1458
    return conditional_prob

cond_prob(df)
