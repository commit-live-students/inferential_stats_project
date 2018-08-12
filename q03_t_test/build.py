# Default imports
from statsmodels.stats.weightstats import ztest
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')

def t_statistic(df):
    z_statistic, p_value = ztest(x1=df[df['Neighborhood'] == 'OldTown']['GrLivArea'], value=df['GrLivArea'].mean())

    #Calculates the T-test for the mean of ONE group of scores.
    pvalue=stats.ttest_1samp(a= df[df['Neighborhood'] == 'OldTown']['GrLivArea'],
                             popmean = df['GrLivArea'].mean())

    test_result=pvalue[1] < p_value
    return pvalue[1],test_result
