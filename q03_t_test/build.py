# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def t_statistic(df):
    ztdata , pv= stats.ttest_1samp(a= df[df['Neighborhood'] == 'OldTown']['GrLivArea'],               # Sample data
                 popmean= df['GrLivArea'].mean())
    p_value90 = stats.norm.ppf(q=0.90)
    
    if(pv<p_value90):
        return pv,np.False_
    else:
        return pv,np.True_

