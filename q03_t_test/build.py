# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import math
#from statsmodels.stats.weightstats import ztest
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def t_statistic(dataframe):
    df = dataframe
    sample_data = df[df['Neighborhood'] == 'OldTown']['GrLivArea']
    pop_mean = df['GrLivArea'].mean()
    results = stats.ttest_1samp(a=sample_data,popmean=pop_mean)
    p_value = results.pvalue
    test_result = results.statistic
    result = p_value < 0.1
    return p_value, result


