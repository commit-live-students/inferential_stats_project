# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def cond_prob(df):
    all_house = df.shape[0]
    house_in_old_town = df[df['Neighborhood']=='OldTown'].shape[0]
    return (house_in_old_town/all_house)**3
    




