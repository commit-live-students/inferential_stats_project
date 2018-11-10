# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here

def cond_prob(df):
    
    Oldtown_count = df[df['Neighborhood']=='OldTown']['Neighborhood'].count()
    Total_count   = df['Neighborhood'].count()

    Pick1_Prob = (Oldtown_count/Total_count)
    Pick2_Prob = (Oldtown_count-1)/(Total_count-1)
    Pick3_Prob = (Oldtown_count-2)/(Total_count-2)
    
    Conditional_Prob = Pick1_Prob*Pick2_Prob*Pick3_Prob
    
    return Conditional_Prob

cond_prob()


