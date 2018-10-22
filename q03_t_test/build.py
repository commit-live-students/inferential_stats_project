# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def t_statistic(df):
    t_test,pval = stats.ttest_1samp(a= df[df['Neighborhood'] == 'OldTown']['GrLivArea'],
                               popmean = df['GrLivArea'].mean())
    if pval < 0.005:
        t_test = np.True_
    else:
        test = np.False_
    return pval, test
t_statistic(df)

