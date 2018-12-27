# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def t_statistic(df):
    z_statistic, p_value = stats.ttest_1samp(a= df[df['Neighborhood'] == 'OldTown']['GrLivArea'], popmean= df['GrLivArea'].mean())
    
    t_stat = stats.norm.ppf(0.9)
    
    if p_value < t_stat:
        test_result = np.False_
    else:
        test_result = np.True_
    
    return p_value, test_result


