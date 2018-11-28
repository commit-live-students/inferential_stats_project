# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
from statsmodels.stats.weightstats import ztest
def t_statistic(df):
    statistic, p_value = stats.ttest_1samp(a= df[df['Neighborhood'] == 'OldTown']['GrLivArea'],               
                 popmean= df['GrLivArea'].mean()) 
    
    pval=np.array(p_value)
    test_result=np.all(pval<0.01)
    return p_value,test_result



