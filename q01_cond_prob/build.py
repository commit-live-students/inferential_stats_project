# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here

def cond_prob(df):
    #df1 = pd.DataFrame()
    all_houses = len(df.index)
    house_in_OldTown = len(df[df['Neighborhood'] == 'OldTown'].index)
    col = (house_in_OldTown/all_houses) * ((house_in_OldTown - 1)/(all_houses - 1)) * ((house_in_OldTown - 2)/(all_houses - 2))
    return col




