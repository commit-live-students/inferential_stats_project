# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def cond_prob(df):

    cnt_oldtown = df.groupby("Neighborhood").size()["OldTown"]

    prob_select1 = cnt_oldtown / len(df)
    prob_select2 = ((cnt_oldtown - 1) / (len(df) - 1))
    prob_select3 = ((cnt_oldtown - 2) / (len(df) - 2))

    return prob_select1 * prob_select2 * prob_select3
