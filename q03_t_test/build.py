# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def t_statistic(df):
    t_statistic, p_value = stats.ttest_1samp(a=df[df['Neighborhood'] == 'OldTown']['GrLivArea'], popmean=df['GrLivArea'].mean())
#     print('Z-statistic is :{}'.format(t_statistic))
#     print('P-value is :{}'.format(p_value))
    if p_value<0.05:
        res= np.True_
    else:
        res=  np.False_
    return p_value,res
