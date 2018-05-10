# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

def cond_prob(df):
    #print(df[df['Neighborhood']=='OldTown'].shape[0])
    OldTownNo=df[df['Neighborhood']=='OldTown'].shape[0]
    TotalHouses=df.shape[0]
    #print(TotalHouses)
    return((OldTownNo/TotalHouses)*((OldTownNo-1)/(TotalHouses-1))*((OldTownNo-2)/(TotalHouses-2)))
#cond_prob()

# Enter Code Here





