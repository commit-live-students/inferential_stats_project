# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def cond_prob(df):
    total_count = df.shape[0]
    house_count = df[df['Neighborhood'] == 'OldTown'].shape[0]
    #print(total_count, house_count)
    conditional_prob = (house_count * (house_count-1) * (house_count-2))/(total_count * (total_count-1) * (total_count-2))
    return conditional_prob

cond_prob(df)
