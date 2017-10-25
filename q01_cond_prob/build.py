# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')

# Enter Code Here
from math import factorial

def permutation(n, r):
	p = factorial(n) / factorial((n - r))
	return p


def combinations(n, r):
	c = factorial(n) / (factorial((n - r)) * factorial(r) )
	return c

def cond_prob(df):
    col_count = df['Neighborhood'].count()
    oldtown_count =  (df['Neighborhood'].str.lower() ==  'oldtown').sum()
    print col_count, oldtown_count

cond_prob(df)
