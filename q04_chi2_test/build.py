# %load q04_chi2_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


def chi_square(df):
    a = df['LandSlope']
    b = pd.qcut(df['SalePrice'],3, labels = ['High','Medium','Low'])
    freq = pd.crosstab(a,b)
    chi2,pval,dog,expected = stats.chi2_contingency(freq)
    return pval, pval < 0.05
