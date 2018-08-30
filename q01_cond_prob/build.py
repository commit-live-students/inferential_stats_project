# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def cond_prob(df):
    probabilty = df['Neighborhood'].value_counts()['OldTown']/sum(df['Neighborhood'].value_counts())*(df['Neighborhood'].value_counts()['OldTown']-1)/(sum(df['Neighborhood'].value_counts())-1)*(df['Neighborhood'].value_counts()['OldTown']-2)/(sum(df['Neighborhood'].value_counts())-2)
    return probabilty
cond_prob(df)




