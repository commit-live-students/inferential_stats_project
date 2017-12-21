from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

def cond_prob(df):
    All_houses = df['Id'].shape[0]
    All_old_town_houses = df[df['Neighborhood'] == 'OldTown'].shape[0]
    conditional_prob = 1
    for i in range(3):
        conditional_prob = conditional_prob * ((All_old_town_houses)/All_houses)
        All_old_town_houses -= 1
        All_houses -= 1

    return conditional_prob
