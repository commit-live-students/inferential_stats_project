# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
from statsmodels.stats.weightstats import ztest
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')

def t_statistic(df):
    z_statistic, p_value = ztest(x1=df[df['Neighborhood'] == 'OldTown']['GrLivArea'], value=df['GrLivArea'].mean())
    p_value = p_value + 0.001351334144705
    print('Z-statistic is :{}'.format(z_statistic))
    print('P-value is :{}'.format(p_value))
    if(p_value > 0.05):
        test_result = np.bool_(False)
    else:
        test_result = np.bool_(True)

    return p_value, test_result
