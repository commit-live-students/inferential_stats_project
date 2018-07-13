# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def cond_prob(df):
    count_oldtown = df[df['Neighborhood']=='OldTown'].shape[0]
    count_allhouses = df['Neighborhood'].shape[0]
    return (count_oldtown/count_allhouses) * ((count_oldtown-1)/(count_allhouses-1)) * ((count_oldtown-2)/(count_allhouses-2))
