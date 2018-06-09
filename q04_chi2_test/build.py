# %load q04_chi2_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def chi_square(df):
    sales_price = pd.qcut(df['SalePrice'], 3, labels = ['High', 'Medium', 'Low'])
    freqtab = pd.crosstab(df.LandSlope,sales_price)
    chi2,p_value,dof,expected = stats.chi2_contingency(freqtab)
    test_result = p_value < 0.05
    return p_value, test_result




