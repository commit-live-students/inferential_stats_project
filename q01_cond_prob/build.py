# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here

def cond_prob(df):
    all_houses = df.shape[0]
    houses_in_OldTown = df[df['Neighborhood'] == 'OldTown'].shape[0]
    conditional_prob=(houses_in_OldTown/all_houses)*((houses_in_OldTown-1)/(all_houses-1))*(houses_in_OldTown-2)/(all_houses-2)
    return conditional_prob

cond_prob(df)
    




