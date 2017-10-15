# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
def t_statistic(df):
    res=stats.ttest_1samp(a= df[df['Neighborhood'] == 'OldTown']['GrLivArea'],               # Sample data
                 popmean= df['GrLivArea'].mean())  # Pop mean
    p_value = res[1]
    if p_value < 0.1:
        test_res=False
    else:
        test_res=True
    return p_value,np.bool_(test_res)
