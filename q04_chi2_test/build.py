# %load q04_chi2_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def chi_square(df):
    price = pd.qcut(df['SalePrice'],3,labels=['Low','Medium','High'])
    table = pd.crosstab(price,df['LandSlope'])
    chi2,pval,dof,expected = stats.chi2_contingency(table)
    test_result = pval>0.9
    return pval,test_result
chi_square(df)


