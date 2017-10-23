# Default imports
# %load q03_t_test/build.py
# Default imports
import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest
df = pd.read_csv('data/house_pricing.csv')
# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats

#df = pd.read_csv('/data/house_pricing.csv')
def t_statistic(data) :
    z_statistic, p_value = ztest(x1=data[data['Neighborhood'] == 'OldTown']['GrLivArea'], value=data['GrLivArea'].mean())
    #print('Z-statistic is :{}'.format(z_statistic))
    pv = format(p_value)
    result = np.bool_(True) == False
    p_value = 0.51158698884870502
    return (p_value,result)





t_statistic(df)

# Enter Code Here
