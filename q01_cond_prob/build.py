# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')
def cond_prob(df):
    df_new = df[df['Neighborhood']=='OldTown']
    prob=(df_new.shape[0] /df.shape[0]) * ((df_new.shape[0] -1) /(df.shape[0]-1))*( (df_new.shape[0]-2) / (df.shape[0]-2) )
    return prob
                               



