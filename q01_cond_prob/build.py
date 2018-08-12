# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def cond_prob(df):
    cot = df[df['Neighborhood'] == 'OldTown'].shape[0]
    ct = df.shape[0]
    c1 = cot / float(ct)
    cot = cot - 1
    ct = ct - 1
    c2 = cot / float(ct)
    cot = cot - 1
    ct = ct - 1
    c3 = cot / float(ct)
    return c1*c2*c3
