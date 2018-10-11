# %load q04_chi2_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')

def chi_square(df):
    price = pd.qcut(df['SalePrice'], 3, labels = ['High', 'Medium', 'Low'])
    freqtab = pd.crosstab(df.LandSlope,price)
    chi2,p_value,dof,expected = stats.chi2_contingency(freqtab)
    test_result=np.all(expected>5)
    return p_value,test_result


