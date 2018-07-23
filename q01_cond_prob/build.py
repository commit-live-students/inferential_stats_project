# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def cond_prob(df):
    oldTownLen = len(df[df['Neighborhood'] == 'OldTown'])
    totalLen = len(df['Neighborhood'])
    print(totalLen)
    conditional_prob = (oldTownLen / totalLen) * ((oldTownLen - 1) / totalLen) * ((oldTownLen-2) / totalLen)
    return conditional_prob
cond_prob(df)




