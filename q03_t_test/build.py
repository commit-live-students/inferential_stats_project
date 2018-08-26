# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import math
import numpy as np
from statsmodels.stats.weightstats import ztest

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def t_statistic(df):
#     sample_mean = df[df['Neighborhood']=='OldTown']['GrLivArea'].mean() 
#     pop_mean = df['GrLivArea'].mean()
#     pop_stdev = df['GrLivArea'].std()
#     sample_size = df[df['Neighborhood']=='OldTown'].shape[0]
#     z = (sample_mean - pop_mean)/((pop_stdev)/math.sqrt(sample_size))    
#     p_value = 1
#     test_result = True
    #z_statistic, p_value = ztest(x1=df[df['Neighborhood'] == 'OldTown']['GrLivArea'], value=df['GrLivArea'].mean())
    z_statistic, p_value = stats.ttest_1samp(a= df[df['Neighborhood'] == 'OldTown']['GrLivArea'], popmean= df['GrLivArea'].mean())
    alpha_val = 1.645 #90% signoficance
    if  p_value < alpha_val:
        test_result = np.False_
    else: 
        test_result = np.True_
    
    return p_value, test_result
    










