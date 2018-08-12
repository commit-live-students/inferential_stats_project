# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def chi_square(df):
    rate = pd.qcut(df['SalePrice'], 3, labels = ['High', 'medium', 'low'])
    #sell = df.pivot_table(index=['LandSlope'], columns=rate, aggfunc=len)
    sell = pd.crosstab(df['LandSlope'], rate)

    #_, p_value, _, _ = stats.chi2_contingency(sell)
    _, p_value, _, _ = stats.chi2_contingency(sell )
    test_result = p_value > 0.5

    return (p_value, test_result)

#print chi_square(df)
