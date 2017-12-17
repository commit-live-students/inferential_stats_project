# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def cond_prob (df):
    oldtown_count= df.Neighborhood.value_counts()['OldTown']
    total= len(df)

    return (oldtown_count/total * (oldtown_count- 1) /(total-1)
            * (oldtown_count -2)/(total-2))

#print cond_prob(df)
