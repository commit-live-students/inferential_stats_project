# %load q03_t_test/build.py
# Default imports
import numpy as np
import scipy.stats as stats
import pandas as pd
data = pd.read_csv('data/house_pricing.csv')

def t_statistic(data):
    z_critical=stats.norm.ppf(q=0.90)
    a=stats.ttest_1samp(a= data[data['Neighborhood'] == 'OldTown']['GrLivArea'],               # Sample data
                 popmean= data['GrLivArea'].mean())
    if a[0]<a[1]:
        b=np.array(a)
        return b[1],b[1]<b[0]
c=t_statistic(data)
c



