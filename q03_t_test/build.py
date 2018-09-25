# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest
df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def t_statistic(df):
    z_statistics,p_value=stats.ttest_1samp(df[df['Neighborhood']=='OldTown']['GrLivArea']
                              ,df['GrLivArea'].mean())
    z_critical = stats.norm.ppf(q = 0.90)
    if(p_value < z_critical):
        return p_value,np.False_
    else:
        return p_value,np.True_


t_statistic(df)




