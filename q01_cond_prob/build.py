# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')
def cond_prob(df):
    return len(df[df['Neighborhood']=='OldTown'])/len(df['Neighborhood'])*(len(df[df['Neighborhood']=='OldTown'])-1)/(len(df['Neighborhood'])-1)*(len(df[df['Neighborhood']=='OldTown'])-2)/(len(df['Neighborhood'])-2)
