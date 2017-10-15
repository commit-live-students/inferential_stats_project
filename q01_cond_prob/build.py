# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

# Enter Code Here
#print(df['Neighborhood'])

def cond_prob(df):
    oldTown_filer=df['Neighborhood']=='OldTown'

    allHouses= df['Neighborhood']
    oldTown_houses=allHouses[oldTown_filer]
    No_of_allHouse=allHouses.shape[0]
    No_of_OldTown=oldTown_houses.shape[0]
    prob=(No_of_OldTown/No_of_allHouse)*((No_of_OldTown-1)/(No_of_allHouse-1))*((No_of_OldTown-2)/(No_of_allHouse-2))
    return prob

#type(cond_prob(df))
