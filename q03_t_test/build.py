# Default imports
import numpy as np
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

# Enter Code Here
def t_statistic(df):
    a = stats.ttest_1samp(a= df[df['Neighborhood'] == 'OldTown']['GrLivArea'], popmean = df['GrLivArea'].mean())  # Pop mean
    p_value = a.pvalue

    t_test = (p_value > 0.9)
    return p_value, t_test
