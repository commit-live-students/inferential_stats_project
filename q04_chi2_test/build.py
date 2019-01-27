# %load q04_chi2_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def chi_square(df):
    salesPrice = pd.qcut(df['SalePrice'], 3, ['High', 'Medium', 'Low'])
    landSlope = df['LandSlope']
    crosstab = pd.crosstab(landSlope, salesPrice)
    chi2,pval,dof,expected = stats.chi2_contingency(crosstab)
    return pval, np.greater(pval, 0.5)


chi_square(df)


