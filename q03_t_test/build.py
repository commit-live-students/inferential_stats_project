# %load q03_t_test/build.py
# Default imports
import scipy.stats as stat
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

def t_statistic(df):
    df=df
    t_stat,pvalue=stat.ttest_1samp(a=df[df['Neighborhood']=='OldTown']['GrLivArea'], popmean=df['GrLivArea'].mean())
    return pvalue,(t_stat>=0.10)#0.10 is the significance value for 90%




