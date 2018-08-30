# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def t_statistic(df):
    z_statistic,p_value = stats.ttest_1samp(a=df[df['Neighborhood']=='OldTown']['GrLivArea'],popmean = df['GrLivArea'].mean())
    test_result = p_value>0.9
    return p_value,test_result
t_statistic(df)


