# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

def cond_prob(df):
    old_town_len = len(df[df['Neighborhood']=='OldTown'])
    total_len = len(df)
    prob_3 = (old_town_len*(old_town_len-1)*(old_town_len-2))/(total_len*(total_len-1)*(total_len-2))
    return prob_3
# Enter Code Here
