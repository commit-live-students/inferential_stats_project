# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd
import numpy as np
count=0
countTotal=0

df = pd.read_csv('data/house_pricing.csv')
def cond_prob(df): 
    Total_OldTown=df[df['Neighborhood']=='OldTown'].shape[0]
    Total_Houses=df['Neighborhood'].shape[0]
    Prob1=Total_OldTown/Total_Houses
    Prob2=(Total_OldTown-1)/(Total_Houses-1)
    Prob3=(Total_OldTown-2)/(Total_Houses-2)
    TotalProb=Prob1*Prob2*Prob3
    return(TotalProb)



