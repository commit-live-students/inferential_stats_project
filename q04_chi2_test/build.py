# %load q04_chi2_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here


#ser, bins = pd.qcut(df['A'], 20, retbins=True, labels=False)

SalePrice_divided, bins = pd.qcut(df['SalePrice'],3,retbins = True, 
                                  labels = False)
#SalePrice_divided
#df.head()
def chi_square(df):
    SalePrice_divided, bins = pd.qcut(df['SalePrice'],3,retbins = True, 
                                  labels = False)
    f_obs = pd.crosstab(df['LandSlope'],SalePrice_divided)
    chi2, p, dof, expected = stats.chi2_contingency(f_obs)

    return p, chi2 < 0.5
chi_square(df)
#chi_square()
SalePrice_divided, bins = pd.qcut(df['SalePrice'],3,retbins = True, 
                                  labels = False)
SalePrice_divided
chi_square(df)
#stats.chi2_contingency(SalePrice_divided)


