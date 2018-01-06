# Default imports
from statsmodels.stats.weightstats import ztest
import scipy.stats as stats
import numpy as np
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def t_statistic(df):
    _, p_value = ztest(
        x1=df[df['Neighborhood'] == 'OldTown']['GrLivArea'],
        value=df['GrLivArea'].mean()
        )

    pvalue = stats.ttest_1samp(
        a=df[df['Neighborhood'] == 'OldTown']['GrLivArea'],
        popmean=df['GrLivArea'].mean()
        )

    test_result = pvalue[1] < p_value
    return pvalue[1], test_result
