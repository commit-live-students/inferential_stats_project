# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')
def cond_prob(rf):
    pOldTown1=len(rf.Neighborhood[rf.Neighborhood=='OldTown'])/len(rf.Neighborhood)
    pOldTown2=(len(rf.Neighborhood[rf.Neighborhood=='OldTown'])-1)/(len(rf.Neighborhood)-1)
    pOldTown3=(len(rf.Neighborhood[rf.Neighborhood=='OldTown'])-2)/(len(rf.Neighborhood)-2)
    return pOldTown1*pOldTown2*pOldTown3

# Enter Code Here





