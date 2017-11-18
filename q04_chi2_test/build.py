# %load q04_chi2_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')

def chi_square(df):
    Land_slope = df['LandSlope']
    Sale_P = pd.qcut(df['SalePrice'],3, labels = ['High','Medium','Low'])
    freqtab = pd.crosstab(Sale_P,Land_slope)
    chi2,p_value,a,b = stats.chi2_contingency(freqtab)
    if chi2 < p_value:
        test_result = True
    else:
        test_result = False

    return p_value, np.bool_(test_result)
#p_value,test_result






# Enter Code Here
