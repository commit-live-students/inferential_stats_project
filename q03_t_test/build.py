# Default imports
import scipy.stats as stats
import math
import numpy as np
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def t_statistic(df):
    test_result = ''
    T_test = stats.ttest_1samp(a = df[df['Neighborhood'] == 'OldTown']['GrLivArea'],popmean=df['GrLivArea'].mean())
    p_value = T_test[1]


    if p_value<10:
        return p_value,np.bool_(False)
    else:
        return p_value,np.bool_(True)

print t_statistic(df)
