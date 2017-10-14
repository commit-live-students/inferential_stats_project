# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

# Enter Code Here

def chi_square(df):
    price=pd.qcut(df['SalePrice'],3,labels=['high','medium','low'])
    r=pd.crosstab(df['LandSlope'],price)
    #print r
    chi2,pval,dof,expected = stats.chi2_contingency(r)
    #print chi2
    #print pval,dof,expected
    #return pval
    result=pval<0.05
    return pval,result
