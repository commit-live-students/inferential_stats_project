# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

def t_statistic(df):

    sample = df[df['Neighborhood']=='OldTown']['GrLivArea']
    t_statistic, p_value = stats.ttest_1samp(a=sample, popmean=df['GrLivArea'].mean())
    return p_value, p_value < 0.05
# Enter Code Here
t_statistic(df)
