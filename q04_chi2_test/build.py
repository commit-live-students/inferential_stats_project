# %load q04_chi2_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def chi_square(df):
    SalesPrice = pd.qcut(df['SalePrice'], 3, labels=['High','medium','low'])
    freqtab = pd.crosstab(df['LandSlope'],SalesPrice)
    chi2,p_value,dof,expected = stats.chi2_contingency(freqtab)
    
    if p_value < 0.05:
        test_result = np.True_
    else:
        test_result = np.False_
    
    return p_value, test_result
    
chi_square(df)




