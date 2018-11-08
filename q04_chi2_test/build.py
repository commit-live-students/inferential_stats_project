# %load q04_chi2_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')
def chi_square(df):
    salesdata=pd.qcut(df['SalePrice'],3,labels=['High', 'Medium', 'Low'])
    p1=pd.Series(salesdata)
    p2=pd.Series(df['LandSlope'])
    chi2,pval,dof,expected=stats.chi2_contingency(pd.crosstab(p1,p2))
    testresult=pval>0.05
    return(pval,testresult)

chi_square(df)

