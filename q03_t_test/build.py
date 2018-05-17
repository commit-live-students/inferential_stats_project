# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
from statsmodels.stats.weightstats import ztest
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here

def t_statistic(data):
    z_statistic, p_value = ztest(x1=data[data['Neighborhood'] == 'OldTown']['GrLivArea'], value=data['GrLivArea'].mean())
    pvalue=stats.ttest_1samp(a= data[data['Neighborhood'] == 'OldTown']['GrLivArea'], popmean= data['GrLivArea'].mean())
    test_result=pvalue[1] < p_value
    return pvalue[1],test_result


