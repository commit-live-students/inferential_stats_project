# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

# Enter Code Here
def cond_prob(df):
    tot_cnt = len(df.index)
    ot_cnt = len(df[df['Neighborhood'] == 'OldTown'])
    result =(ot_cnt / tot_cnt) * ((ot_cnt-1) / (tot_cnt -1)) * ((ot_cnt-2) / (tot_cnt -2))
    return result
