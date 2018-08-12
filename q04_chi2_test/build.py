# %load q04_chi2_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def chi_square(df):    
    price = pd.qcut(df['SalePrice'], 3, labels = ['High', 'Medium', 'Low'])
    chi2,pval,dof,expected = stats.chi2_contingency(pd.crosstab(df.LandSlope, price))
    #print pd.crosstab(df.LandSlope, price)
    return float(pval), pval < 0.05

chi_square(df)


