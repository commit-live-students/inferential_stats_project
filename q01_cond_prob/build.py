# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')
def cond_prob(df):
    all_houses = df.shape[0]
    houses_in_OldTown = df[df['Neighborhood'] == 'OldTown']
    first_prob =  (houses_in_OldTown.shape[0]/all_houses)
    sec_prob  = first_prob * ((houses_in_OldTown.shape[0] - 1)/(all_houses - 1))
    final = (sec_prob * ((houses_in_OldTown.shape[0] - 2)/(all_houses - 2)))
    return (final)
