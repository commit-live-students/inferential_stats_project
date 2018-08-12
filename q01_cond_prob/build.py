# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def cond_prob(df):
    all_houses=df.shape[0]
    houses_in_OldTown=df[df.Neighborhood=='OldTown'].shape[0]
    distinct_neighborhood=df.Neighborhood.value_counts()
    picking_first_house=houses_in_OldTown/all_houses
    picking_second_house=(houses_in_OldTown-1)/(all_houses-1)
    picking_third_house=(houses_in_OldTown-2)/(all_houses-2)
    tot_pblity=picking_first_house*picking_second_house*picking_third_house
    return(tot_pblity)
