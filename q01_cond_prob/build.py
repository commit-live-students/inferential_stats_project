# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def cond_prob(df):

    # number of ho
    total_house_in_oldtown = len(df[df['Neighborhood']== 'OldTown']) # number of house in oldtown
    total_house = len(df)  # total number of house

    #calculate conditional probability 
    cond_probability = ((total_house_in_oldtown)/(total_house))*((total_house_in_oldtown-1)/(total_house-1)) * ((total_house_in_oldtown-2)/(total_house-2))

    return cond_probability







cond_prob(df)


