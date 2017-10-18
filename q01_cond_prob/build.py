# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

def cond_prob(df):
    allnh = df.loc[:,'Neighborhood']

    allnhcount = allnh.count()
    filter1 = allnh == 'OldTown'
    oldtownnh = df['Neighborhood'][filter1]
    oldtownnhcount = oldtownnh.count()
    
    cp = oldtownnhcount/allnhcount * (oldtownnhcount - 1)/(allnhcount-1) * (oldtownnhcount - 2)/(allnhcount - 2)
    return cp






# Enter Code Here
