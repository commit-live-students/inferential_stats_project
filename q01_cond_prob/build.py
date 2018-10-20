# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')



# Enter Code Here
def cond_prob(df):
    no_of_houses = len(df)
    oldTown_houses = len(df[df['Neighborhood'] ==' OldTown'])
    conditional_prob = (oldTown_houses/no_of_houses)*((oldTown_houses-1)/(no_of_houses-1))*((oldTown_houses-2)/(no_of_houses-2))
    return conditional_prob



