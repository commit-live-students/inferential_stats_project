# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here

def cond_prob(df):
    th = df.shape[0]
    ho = df[df['Neighborhood']=='OldTown'].shape[0]
    conditional_prob = (ho/th)*((ho-1)/(th-1))*((ho-2)/(th-2))
    return conditional_prob
