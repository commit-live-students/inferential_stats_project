# %load q04_chi2_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def chi_square(df):
    price_category = pd.qcut(df['SalePrice'], 3, labels = ['High', 'Medium', 'Low'])    
    freqtab = pd.crosstab(df.LandSlope,price_category)
    chi2, pval, dof, expected = stats.chi2_contingency(freqtab)
    return pval, pval<0.05
    
chi_square(df)

