# %load q04_chi2_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

df = pd.read_csv('data/house_pricing.csv')


def chi_square(df):
    sale_price = pd.qcut(df['SalePrice'],3, labels=['high', 'medium', 'low'])
    land_slope = df['LandSlope']
    df_combined = pd.concat([sale_price, land_slope], axis=1)
    chi_result = chi2_contingency(pd.crosstab(sale_price,land_slope))
    test_result = np.False_
    if chi_result[1] < 0.05:
        test_result = np.True_
    return (chi_result[1], test_result)

