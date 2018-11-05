# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')

def t_statistic(df):
    houses_OLDT = df[df['Neighborhood']=='OldTown'].GrLivArea
    p_value = (stats.ttest_1samp(a =houses_OLDT , popmean=df.GrLivArea.mean())).pvalue
    x= (stats.ttest_1samp(a=df.GrLivArea,popmean=df.GrLivArea.mean())).statistic
    t = stats.t.cdf(x,df=49)
    return p_value, np.bool_(t > p_value)





