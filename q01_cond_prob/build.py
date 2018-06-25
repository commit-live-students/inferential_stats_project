# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

# Enter Code Here
def cond_prob(dataframe):
    all_houses = dataframe.shape[0]
    old_town_houses = dataframe[dataframe['Neighborhood'] == 'OldTown']
    all_old_town_houses = old_town_houses.shape[0]
    
    prob_1 = (all_old_town_houses)/(all_houses)
    prob_2 = (all_old_town_houses - 1)/(all_houses - 1)
    prob_3 = (all_old_town_houses - 2)/(all_houses - 2)
    
    probability = prob_1 * prob_2 * prob_3
    return probability

output = cond_prob(df)
print(output)

