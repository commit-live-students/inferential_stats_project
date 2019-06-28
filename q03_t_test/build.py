# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import math
import numpy as np


df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here

def t_statistic(df):
    t_statistic, p_value = stats.ttest_1samp(a=df[df['Neighborhood'] == 'OldTown']['GrLivArea'], popmean=df['GrLivArea'].mean())
    print(('Z-statistic is :{}'.format(t_statistic)))
    print(('P-value is :{}'.format(p_value)))
    tStatsVal = stats.norm.ppf(0.9)
    print(tStatsVal)
    returnBool = False
    if p_value < tStatsVal:
        returnBool = np.False_
    else:
        returnBool = np.True_
    
    return p_value,returnBool
p_val, result = t_statistic(df)
print(type(result))
print(result)
print(pval)



