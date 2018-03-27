# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest
df = pd.read_csv('data/house_pricing.csv')
bol = np.bool_(dtype=bool)
# Enter Code Here
def t_statistic(data):
    #z_statistic, p_value = ztest(x1=data[data['Neighborhood'] == 'OldTown']['GrLivArea'], value=data['GrLivArea'].mean())
    z_statistic,p_value= stats.ttest_1samp(a= data[data['Neighborhood'] == 'OldTown']['GrLivArea'],
                 popmean= data['GrLivArea'].mean())
    if z_statistic <=0.05:
        bol = np.bool_(False)
    else:
        bol =  np.bool_(True)
    return p_value, bol
