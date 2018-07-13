# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def cond_prob(df):
    cnt=len(df)
    cnt1=len(df.loc[df['Neighborhood']=='OldTown'])
    res=( (cnt1*(cnt1-1)*(cnt1-2))/ (cnt*(cnt-1)*(cnt-2)) )
    return res
