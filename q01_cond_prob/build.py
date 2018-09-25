# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')
# Enter Code Here
def cond_prob(df):
    tot_count=df.iloc[:,0].count()
    old_count=df[df.loc[:,'Neighborhood']=='OldTown'].iloc[:,0].count()
    con_prob=(old_count/tot_count)*((old_count-1)/(tot_count-1))*((old_count-2)/(tot_count-2))
    return con_prob

cond_prob(df)





