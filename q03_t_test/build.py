# %load q03_t_test/build.py
# Default imports

import scipy.stats as stats
from scipy.stats import t
import pandas as pd
import numpy
df = pd.read_csv('data/house_pricing.csv')

from statsmodels.stats.weightstats import ztest

def t_statistic(df):
    deg_freedom = df['Neighborhood'].value_counts()['OldTown']-1
    p=0.90
    value = t.ppf(p,deg_freedom)
    result,p_value =stats.ttest_1samp(a= df[df['Neighborhood'] == 'OldTown']['GrLivArea'], popmean= df['GrLivArea'].mean())
    test_result=result>value
    return float(p_value),test_result

t_statistic(df)





