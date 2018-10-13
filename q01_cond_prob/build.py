from __future__ import division
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

def cond_prob(df):
    allhouses = df.shape[0]
    houses_in_OldTown = df[df['Neighborhood'] == 'OldTown'].shape[0]
    n = (houses_in_OldTown)*(houses_in_OldTown-1)*(houses_in_OldTown-2)
    k = ( allhouses)*(allhouses-1)*(allhouses-2)
    probofthree = float(n/k)
    
    return probofthree
    
cond_prob(df)





