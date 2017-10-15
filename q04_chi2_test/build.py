# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')

# Enter Code Here
def chi_square(df):
    landS = df['LandSlope']
    saleP = pd.qcut(df['SalePrice'],3,['High', 'Medium', 'Low'])
    freq = pd.crosstab(landS,saleP)
    chi2,pval,dof,expected = stats.chi2_contingency(freq)

    if pval < 0.05:
        test_result = True
    else:
        test_result = False

    return float(pval),np.bool_(test_result)
