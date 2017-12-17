# So that float division is by default in python 2.7
from __future__ import division
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')
def cond_prob(df):
    Total_outcome = len(df)
    fav_outcome = df.groupby('Neighborhood').size()['OldTown']
    #print df['Neighborhood'].unique()
    #for i in df['Neighborhood'].unique():
        #print i,'=', df.groupby('Neighborhood').size()[i]/Total_outcome
    prob1=1
    for i in range(3):
        prob1 = ((fav_outcome-i)/(Total_outcome-i))*prob1
    return prob1

# Enter Code Here
