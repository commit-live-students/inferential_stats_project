# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def cond_prob(df):
    oldtown=(sum(df['Neighborhood']=='OldTown'))
    total=(df['Neighborhood'].count())
    result=(oldtown/total)*((oldtown-1)/(total-1))*((oldtown-2)/(total-2))
    return(result)
#cond_prob(df)





