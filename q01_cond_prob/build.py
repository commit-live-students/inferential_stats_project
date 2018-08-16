# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

def cond_prob(data):
    all_houses = data.shape[0]
    houses_in_OldTown = data[data['Neighborhood'] =='OldTown'].shape[0]
    conditional_prob =(houses_in_OldTown/all_houses)*(houses_in_OldTown - 1)/(all_houses - 1)*((houses_in_OldTown - 2)/(all_houses - 2))
    return float(conditional_prob)

cond_prob(df)






