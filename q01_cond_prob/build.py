# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

def cond_prob(df):
    A=df[df['Neighborhood']=='OldTown'].shape[0]
    B=df.shape[0]
    conditional_prob=(A/B)*((A-1)/(B-1))*((A-2)/(B-2))
    return conditional_prob





