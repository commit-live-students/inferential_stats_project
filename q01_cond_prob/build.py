# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')
# Enter Code Here

def cond_prob(df):
    total = df['Neighborhood'].count()
    oldtown = df[df['Neighborhood']=='OldTown']['Neighborhood'].count()
    conditional_prob = (oldtown/total) * ((oldtown - 1)/(total - 1)) * ((oldtown - 2) / (total - 2))

    return conditional_prob

