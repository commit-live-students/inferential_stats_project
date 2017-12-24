# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def cond_prob(df):
    # 3 houses successfully in old town
    # total no of houses
    total = df.size

    # total no of houses in oldtown
    oldtown = df[df['Neighborhood'] == 'OldTown'].size

    # Event A - pick a house in oldtown
    # Event B - pick another house in oldtown
    # event C - pick another house in Oldtown

    # P(A|B|C) = P(A) * P(B) * P(C)
    # P(Event A) = # of +ve outcomes / # total outcomes
    # print oldtown / total

    #P(A|B}C) =  9153/118260 * 9152/118260 * 9151/118260
    return (oldtown/total) * (oldtown-1)/total * (oldtown-2)/total

    #0.04% - very unlikely

# print cond_prob(df)
# print type(cond_prob(df))
