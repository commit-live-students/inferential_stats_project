# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def cond_prob(df):
    total_houses = float(len(df.index))
    oldtown_houses = float(len(df[df["Neighborhood"] == "OldTown"]))
    proba = (oldtown_houses / total_houses) * ((oldtown_houses-1)/(total_houses-1)) * ((oldtown_houses-2)/(total_houses-2))
    return proba

cond_prob(df)
