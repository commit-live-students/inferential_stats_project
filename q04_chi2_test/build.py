# %load q04_chi2_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def chi_square(df):
    sale_cat = pd.qcut(df['SalePrice'],3,labels=['High','medium','low'])
    chi2_conti = pd.crosstab(df['LandSlope'], sale_cat)
    _, p_value, _, _ = stats.chi2_contingency(chi2_conti)
    if p_value >= 0.05:
        test_result = np.False_
    else:
        test_result = np.True_
    return p_value,test_result



