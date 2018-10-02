# %load q04_chi2_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import scipy.stats as sp
import numpy as np

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def chi_square(df):
    price = pd.qcut(df['SalePrice'], 3, labels = ['High', 'Medium', 'Low'])
    freqtab = pd.crosstab(df.LandSlope,price)
    chi2,p_value,dof,expected = sp.chi2_contingency(freqtab)
    significance = 0.05
    p_value = float(p_value)
    test_result = 1 if p_value <= significance else 0
    test_result = np.bool_(test_result)
        
    return p_value, test_result


