# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here


def cond_prob(df):
    df1 = df[df['Neighborhood']=='OldTown']['Neighborhood'].count()
    df2 = df.shape[0]
    conditional_prob = (df1/df2)*((df1-1)/(df2-1))*((df1-2)/(df2-2))

    return conditional_prob
