# %load q04_chi2_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def chi_square(df):
    price = pd.qcut(df['SalePrice'], 3, labels = ['High', 'Medium', 'Low'])
    frequ_tab = pd.crosstab(df.LandSlope,price)
    chi2,p_value,dof,expected = stats.chi2_contingency(frequ_tab)
    if p_value < 0.05:
        test_result = np.True_
    else:
        test_result = np.False_

    return p_value,test_result    
chi_square(df)




