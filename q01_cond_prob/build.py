# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


def cond_prob(df):
    total = df.shape[0]
    oldtown = df[df.Neighborhood == "OldTown"].shape[0]

    p = (oldtown/total)*((oldtown -1)/(total -1))*((oldtown-2)/(total-2))
    return p
