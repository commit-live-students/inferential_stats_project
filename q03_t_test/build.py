# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
from statsmodels.stats.weightstats import ztest

df = pd.read_csv('data/house_pricing.csv')

# Enter Code Here
def t_statistic(df):
    z_statistic, p_value = ztest(x1=df[df['Neighborhood'] == 'OldTown']['GrLivArea'], value=df['GrLivArea'].mean())
    pvalue=stats.ttest_1samp(a= df[df['Neighborhood'] == 'OldTown']['GrLivArea'],popmean= df['GrLivArea'].mean())
    test_result=pvalue[1] < p_value
    return pvalue[1],test_result

t_statistic(df)



