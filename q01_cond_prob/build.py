# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

# Enter Code Here
def cond_prob(house_df):
    flt_oldtown= house_df["Neighborhood"]=="OldTown"
    a = len(house_df[flt_oldtown])
    b = len(house_df["Neighborhood"])
    prob = (a / b) * ((a-1) / (b-1)) *  ((a-2) / (b-2))
    return prob
