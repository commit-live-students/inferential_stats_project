# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def cond_prob(df):
    total = df['Id'].count()
    df1 = df[df['Neighborhood']=='OldTown']
    old_total = df1['Id'].count()
    old_total2 = old_total - 1
    old_total3 = old_total - 2
    prob_res = (old_total * old_total2 * old_total3) / (total*(total-1)*(total-2))
    return prob_res
cond_prob(df)    



