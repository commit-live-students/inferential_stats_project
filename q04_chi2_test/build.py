# %load q04_chi2_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')

# Enter Code Here
def chi_square(df):
    price = pd.qcut(df['SalePrice'], 3, labels = ['High', 'Medium', 'Low'])
    freqtab = pd.crosstab(df.LandSlope,price)
    chi2,pval,dof,expected = stats.chi2_contingency(freqtab)
    
    if pval < 0.005:
        chi2 = np.True_
    else:
        chi2 = np.False_
    return pval, chi2

chi_square(df)

