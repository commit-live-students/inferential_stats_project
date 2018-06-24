# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

from unittest import TestCase

df = pd.read_csv('data/house_pricing.csv')


def t_statistic(df):
    start = 0
    oldtown_data = df [ df['Neighborhood'] == 'OldTown']['GrLivArea']
    pop_mean = df['GrLivArea'].mean()
    results = stats.ttest_1samp(a=oldtown_data,popmean=pop_mean)
    pvalue = results.pvalue
    if pvalue < 0.9:
        ans = np.False_
    else:
        ans = np.True_
    return pvalue, ans

