# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

def cond_prob(df):
    total_n = df.shape[0]
    old_town = df[df['Neighborhood'] == 'OldTown'].shape[0]
    conditional_prob = float((old_town/total_n)*((old_town-1)/(total_n-1))*((old_town-2)/(total_n-2)))
    return conditional_prob


# Enter Code Here
