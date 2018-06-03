# %load q04_chi2_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def chi_square(df):
    df['qcutResult'] = pd.qcut(df['SalePrice'], 3, labels=['High', 'medium', 'low'])
    freqTab = pd.crosstab(df['LandSlope'],df['qcutResult'])
    chi2,pval,dof,expected = stats.chi2_contingency(freqTab)
    #print(chi2,pval,dof,expected)
    
    crit = stats.chi2.ppf(q = 0.95,df=2)
    print(crit)
    boolRet = False
    if pval > crit:
        boolRet = np.True_
    else:
        boolRet = np.False_
    
    return  pval,boolRet
chi_square(df)

