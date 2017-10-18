# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

def cond_prob(df):
    total_houses = df.shape[0]
    df1 = df[df["Neighborhood"]=="OldTown"]
    houses_oldTown = df1.shape[0]
    p1 = (houses_oldTown/total_houses) * ((houses_oldTown-1)/(total_houses-1))* ((houses_oldTown-2)/(total_houses-2))
    return p1
