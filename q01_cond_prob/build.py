# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def cond_prob(df):
    '''Function to calaculate conditional probability'''
    #intitalizing the successive count needed 
    n = 3
    i=0
    
    #Count of number of total and oldtown houses from dataset
    df['SalePrice'].shape[0]
    c_neigh = df[df['Neighborhood'] == 'OldTown'].shape[0]
    c_total = df.shape[0]

    #loop to calulate successive probability for n successions
    while i < n:
        p_= (c_neigh - i)/(c_total - i)
        if i == 0:
            conditional_prob = p_
        else:
            conditional_prob = conditional_prob*p_
        i+=1
    return conditional_prob 

#Call the function
cond_prob(df)






