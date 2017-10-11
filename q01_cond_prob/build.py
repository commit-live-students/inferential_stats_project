from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def cond_prob(DataFrame):
    all_houses = df.shape[0]
    houses_in_OldTown = df[df['Neighborhood'] == 'OldTown'].shape[0]
    return (houses_in_OldTown/all_houses) * ((houses_in_OldTown - 1)/(all_houses - 1)) * ((houses_in_OldTown - 2)/(all_houses - 2))
