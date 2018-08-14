# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd,numpy as np

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def t_statistic(df):
    t_stat, p_value =stats.ttest_1samp(a= df[df['Neighborhood'] == 'OldTown']['GrLivArea'],               # Sample data
                 popmean= df['GrLivArea'].mean())
    
    p_crit = stats.norm.ppf(q=0.90)
    if(p_value<p_crit):
        return p_value,np.False_
    else:
        return p_value,np.True_


