# %load q04_chi2_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

# Enter Code Here
def chi_square(df):
    price = pd.qcut(df['SalePrice'], 3, labels = ['High', 'Medium', 'low'])
    freqtab = pd.crosstab(df['LandSlope'],price)
    chi2,pval,dof,expected = stats.chi2_contingency(freqtab)
    
    if pval < .05 :
        test_result =True
    else :
         test_result =False
        
    
    return pval , test_result
    


