# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def cond_prob(df):
    u,counts=np.unique(df['Neighborhood'].values,return_counts=True)
    d=dict(zip(u,counts))
    conditional_prob=(d['OldTown']/sum(counts))*((d['OldTown']-1)/(sum(counts)-1))*((d['OldTown']-2)/(sum(counts)-2))
    
    return conditional_prob



