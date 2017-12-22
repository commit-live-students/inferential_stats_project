# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

def chi_square(df):
    price = pd.qcut(df['SalePrice'], 3, labels = ['High', 'Medium', 'Low'])
    freqtab = pd.crosstab(df['LandSlope'],price)

    chi2,pval,dof,expected = stats.chi2_contingency(freqtab)
    test_result=pval>0.5

    return pval,test_result
