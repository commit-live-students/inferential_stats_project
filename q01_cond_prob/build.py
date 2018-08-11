# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def cond_prob(df):
    total_rows = df.shape[0]
    old_town_rows = df[df['Neighborhood'] == 'OldTown'].shape[0]
    return (old_town_rows / total_rows) * ((old_town_rows - 1)/(total_rows-1)) * ((old_town_rows-2) / (total_rows - 2))



