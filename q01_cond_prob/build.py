# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

def cond_prob(df):
    data = df['Neighborhood']
    total_house_oldtown =  data.value_counts()['OldTown']
    total_house = len(data)
    conditional_prob = (total_house_oldtown/total_house)*((total_house_oldtown - 1)/(total_house - 1))*((total_house_oldtown - 2)/(total_house - 2))
    return conditional_prob

cond_prob(df)
# Enter Code Here
