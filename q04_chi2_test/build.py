# %load q04_chi2_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')
def chi_square(df):
    pr=pd.qcut(df['SalePrice'],3,labels=['High','Medium','Low'])
# Enter Code Here
    freqtab=pd.crosstab(df['LandSlope'],pr)
#print freqtab
    chi2,pval,dof,expected = stats.chi2_contingency(freqtab)
    if pval < 0.05:
        test_res=True
    else:
        test_res=False
    return float(pval),np.bool_(test_res)
