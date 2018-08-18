# %load q04_chi2_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')
def chi_square(data):
    x = data.LandSlope
    y = pd.qcut(data['SalePrice'], 3, labels = ['High', 'Medium', 'Low'])
    
    freqtable = pd.crosstab(x,y)
    chi2,pval,dof,expected = stats.chi2_contingency(freqtable)
    crit = stats.chi2.ppf(q = 0.95, df = dof)
    test_result = crit < chi2

    return pval , test_result

chi_square(df)





