# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

# Enter Code Here
def cond_prob(dataframe):
    conditional_prob = 0
    totalHouses = dataframe.shape[0]
    oldTownHouses = dataframe[dataframe['Neighborhood'] == 'OldTown'].shape[0]
    #print(totalHouses)
    #print(oldTownHouses)
    conditional_prob = (oldTownHouses/totalHouses)*((oldTownHouses-1)/(totalHouses-1))*((oldTownHouses-2)/(totalHouses-2))
    return conditional_prob




