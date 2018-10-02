# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def t_statistic(df):
    stat_values = stats.ttest_1samp(a= df[df['Neighborhood'] == 'OldTown']['GrLivArea'],               # Sample data
                 popmean= df['GrLivArea'].mean())  # Pop mean
    
    significance = 0.1
    p_value = float(stat_values[1])
    test_result = 1 if p_value <= significance else 0
    test_result = np.bool_(test_result)
    return p_value, test_result






