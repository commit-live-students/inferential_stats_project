# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')

def cond_prob(df):
    a = df[df['Neighborhood']=='OldTown']['Neighborhood'].count()
    b = df.shape[0]
    conditional_prob = (a/b)*((a-1)/(b-1))*((a-2)/(b-2))

    return conditional_prob
