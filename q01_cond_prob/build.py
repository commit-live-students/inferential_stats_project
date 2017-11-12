# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

# Enter Code Here
def cond_prob(df):
    for_outcomes = df[df['Neighborhood'] == 'OldTown'].shape[0]
    sample_space = df.shape[0]
    steps = 3
    p = 1
    for i in range(0, steps):
        p = p * ((for_outcomes - i)/(sample_space - i))
        
    return p
