# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

# Enter Code Here
import numpy as np
def chi_square(df):
    land_slope = df['LandSlope']
    sales_price = df['SalePrice']
    sp_cat = pd.qcut(sales_price,3)
    freqtab = pd.crosstab(land_slope,sp_cat)
#     print("Frequency table")
#     print("============================")
#     print(freqtab)
#     print("============================")
    chi2,pval,dof,expected = stats.chi2_contingency(freqtab)
#     print("ChiSquare test statistic: ",chi2)
#     print("p-value: ",pval)
    H0 = np.bool_(True)
    if pval > 0.05:
        H0 = np.bool_(False)
    return pval, H0
#print chi_square(df)
