# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

# Enter Code Here

def get_prob(f_outs, ss, steps):
    p = 1
    for i in range(0, steps):
        p = p * ((f_outs - i)/(ss - i))
    return p
def cond_prob(df):
    for_outcomes = df[df['Neighborhood'] == 'OldTown'].shape[0]
    sample_space = df.shape[0]
    steps = 3
    return get_prob(for_outcomes, sample_space, steps)
