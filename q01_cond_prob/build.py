# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')
def cond_prob(df):
    total=df.shape[0]
    old_house = df[df['Neighborhood']=='OldTown'].shape[0]
    return(old_house/total)*((old_house-1)/(total-1))*((old_house-2)/(total-2))
    
    
    #return( rating_probs)



cond_prob(df)



