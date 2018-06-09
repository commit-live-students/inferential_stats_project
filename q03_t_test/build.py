# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def t_statistic(data):
    res=stats.ttest_1samp(a= data[data['Neighborhood'] == 'OldTown']['GrLivArea'],               # Sample data
                 popmean= data['GrLivArea'].mean()) 
    p_value = 0.90
    if(res.pvalue < p_value):
        boo=np.bool_(False)
    return res.pvalue,boo


t_statistic(df)

