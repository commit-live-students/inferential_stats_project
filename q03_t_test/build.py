# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import math
from statsmodels.stats.weightstats import ztest

df = pd.read_csv('data/house_pricing.csv')

def t_statistic(df):
    #z_statistic, p_value = ztest(x1=df[df['Neighborhood']=='OldTown']['GrLivArea'], value=df['GrLivArea'].mean())
    z_statistic, p_value = stats.ttest_1samp(df[df['Neighborhood']=='OldTown']['GrLivArea'],df['GrLivArea'].mean())
    print(z_statistic)
    return p_value,p_value<0.1  #As significance level is 90% hence 0.1

t_statistic(df)


