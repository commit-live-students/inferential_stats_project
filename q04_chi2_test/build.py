# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def chi_square(data):
    price = pd.qcut(data['SalePrice'], 3, labels = ['High', 'Medium', 'Low'])
    freqtab = pd.crosstab(data.LandSlope,price)
    chi2,pval,dof,expected = stats.chi2_contingency(freqtab)
    test_result=pval>0.5
    return pval,test_result
