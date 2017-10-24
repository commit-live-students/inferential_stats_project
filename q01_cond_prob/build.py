# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')
#print(df)

def cond_prob (df):

    all_houses = df.shape[0]
    houses_in_OldTown = df[df['Neighborhood'] == 'OldTown'].shape[0]
    s1=(houses_in_OldTown/all_houses)* ((houses_in_OldTown-1)/(all_houses-1))*((houses_in_OldTown-2)/(all_houses-2))
    return(s1)

cond_prob (df)
