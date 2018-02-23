# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def cond_prob(df):

    all_houses = df.shape[0]
    houses_in_oldtown = df[df['Neighborhood']=='OldTown'].shape[0]
    conditional_prob =  float((houses_in_oldtown/all_houses)*((houses_in_oldtown-1)/(all_houses-1))*((houses_in_oldtown-2)/(all_houses-2)))
    #print('Probablity of getting 3 houses in row in Oldtown : {}'.format(conditional_prob))
   # print type(conditional_prob)
    return conditional_prob

#print cond_prob(df)
