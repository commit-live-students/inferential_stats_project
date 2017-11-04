# Default imports
import scipy.stats as stats
import pandas as pd
from statsmodels.stats.weightstats import ztest

df = pd.read_csv('data/house_pricing.csv')

# Enter Code Here
def t_statistic(df):
    t_test, p_val = stats.ttest_1samp(a = df[df['Neighborhood'] == 'OldTown']['GrLivArea'], popmean = df['GrLivArea'].mean())
    pval, result = (p_val, p_val<0.1)
    return pval, result
