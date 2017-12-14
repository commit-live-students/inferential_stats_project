# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

def cond_prob(df):
    oldtown=(df['Neighborhood']=='OldTown').sum()
    total=df['Neighborhood'].count()
    #conditional_prob=
    return (oldtown/total)*((oldtown-1)/(total-1))*((oldtown-2)/(total-2))
       
# Enter Code Here
