# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest
from scipy import stats


df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def t_statistic(df):
    q = (1- 0.90)
    t_mean = df['GrLivArea'].mean()
    mean = df[df['Neighborhood']=='OldTown']['GrLivArea'].mean()
    std = df[df['Neighborhood']=='OldTown']['GrLivArea'].std()
    n = df[df['Neighborhood']=='OldTown']['GrLivArea'].shape[0]

    z = abs((mean - t_mean)/(std/(n)**0.5))
    crit = stats.norm.ppf(q=q)
    p_value = stats.norm.sf(z)*2

    z_statistic, p_value = ztest(x1 = df[df['Neighborhood']=='OldTown']['GrLivArea'], value=df['GrLivArea'].mean())
    a = stats.ttest_1samp(a=df[df['Neighborhood']=='OldTown']['GrLivArea'],popmean=df['GrLivArea'].mean())
    if z > crit: 
        return a[1], np.bool_(False)
    else:
        return a[1], np.bool_(True)

t_statistic(df)







