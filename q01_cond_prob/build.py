# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def cond_prob(df):
    all_houses = df.shape[0]
    houses_in_old_town = df[df['Neighborhood'] == 'OldTown']
    num_of_houses_in_old_town = houses_in_old_town.shape[0]
    conditional_prob = (num_of_houses_in_old_town/all_houses) * ((num_of_houses_in_old_town - 1)/(all_houses -1)) * ((num_of_houses_in_old_town - 2)/(all_houses - 2))
    return conditional_prob

cond_prob(df)



