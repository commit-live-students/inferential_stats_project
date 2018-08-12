# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here

def cond_prob(df):
    total_houses = df.shape[0]
    houses_in_oldtown = df[df['Neighborhood'] == 'OldTown'].shape[0]
    houses_in_oldtown = float(houses_in_oldtown)
    conditional_prob = (houses_in_oldtown/total_houses)*((houses_in_oldtown-1)/(total_houses-1))*((houses_in_oldtown-2)/(total_houses-2))
    return conditional_prob
