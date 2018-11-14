# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import numpy as np
import pandas as pd
from statsmodels.stats.weightstats import ztest
df = pd.read_csv('data/house_pricing.csv')

def t_statistic(df):
    statistic, p_value = stats.ttest_1samp(a= df[df['Neighborhood'] == 'OldTown']['GrLivArea'],               
                 popmean= df['GrLivArea'].mean()) 
    
    pval=np.array(p_value)
    test_result=np.all(pval<0.01)
    return p_value,test_result
   


