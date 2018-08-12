# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
from statsmodels.stats.weightstats import ztest
import numpy as np
def t_statistic(df):
    old_town = df[df['Neighborhood'] == 'OldTown']
    pop_mean = df['GrLivArea'].mean()
    p_val = stats.ttest_1samp(a=old_town['GrLivArea'], popmean=pop_mean)[1]
    test_result =  np.bool_(True)
    if p_val > 0.05:
        test_result = np.bool_(False)
    return p_val.item(), test_result

# p,r = t_statistic(df)
# print p
# print r
# print type(p)
# print type(r)
