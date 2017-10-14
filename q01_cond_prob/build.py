# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')
def cond_prob(df):
    total_houses= df.shape[0]
    fil1=df.loc[:,'Neighborhood']=='OldTown'
    houses_old_town=df.loc[fil1,'Neighborhood'].shape[0]

    cond_probability=(houses_old_town/total_houses)*((houses_old_town-1)/(total_houses-1))*((houses_old_town-2)/(total_houses-2))
    #print(type(cond_probability))
    return cond_probability
# Enter Code Here

#cond_prob(df)
