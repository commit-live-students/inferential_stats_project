# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

# Enter Code Here
def cond_prob(df):
    all_houses = df.shape[0]
    old_town_houses = df[df['Neighborhood']=='OldTown'].shape[0]
    conditional_prob = (old_town_houses/all_houses)*((old_town_houses-1)/(all_houses-1))*((old_town_houses-2)/(all_houses-2))
    return conditional_prob
