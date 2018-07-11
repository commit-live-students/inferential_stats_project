# %load q04_chi2_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def chi_square(dataframe):
    df = dataframe
    SalesPriceCat = pd.qcut(df['SalePrice'],3,labels=['Low','Medium','High'])
    landslopeCat = df['LandSlope']
    freqtab = pd.crosstab(landslopeCat,SalesPriceCat)
    chi2,pval,dof,expected = stats.chi2_contingency(freqtab)
    test_result = pval < 0.1
    return pval , test_result # p_value,test_result





