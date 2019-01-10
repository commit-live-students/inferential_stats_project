# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd,numpy as np

df = pd.read_csv('data/house_pricing.csv')
df = pd.DataFrame(df)

from statsmodels.stats.weightstats import ztest
# Enter Code Here
def t_statistic(df):
    statistic, p_value = stats.ttest_1samp(a= df[df['Neighborhood'] == 'OldTown']['GrLivArea'],popmean= df['GrLivArea'].mean()) 
    pval=np.array(p_value)
    test_result=np.all(pval<0.01)
    return p_value,test_result


t_statistic(df)



