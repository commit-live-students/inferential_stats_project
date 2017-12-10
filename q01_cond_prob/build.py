# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here

def cond_prob(df):
    #old_town = df.loc[:,'']
    all_houses = df.shape[0]
    house_old_town = df[df['Neighborhood']=='OldTown'].shape[0]
    #print house_old_town
    #print all_houses
    #print len(df)
    conditional_prob = ((house_old_town/all_houses) * (((house_old_town - 1)/(all_houses - 1)) * ((house_old_town - 2)/(all_houses - 2))))
    return conditional_prob
