### %load q04_chi2_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def chi_square(df):
    land_slope = df['LandSlope']
    sale_price = pd.qcut(df['SalePrice'],3,labels=['High','Medium','Low'])
    input_chi = pd.crosstab(land_slope,sale_price)
    chi2,p,dof,expected = stats.chi2_contingency(input_chi)
    test_res = p < 0.05
    return p,test_res
chi_square(df)


