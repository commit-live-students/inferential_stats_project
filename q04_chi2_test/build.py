# %load q04_chi2_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def chi_square(df):
    price = pd.qcut(df['SalePrice'], 3, labels = ['High', 'Medium', 'Low'])
    LandSlope = df['LandSlope']
    freqtab = pd.crosstab(price,LandSlope)
    print(freqtab)
    chi2,pval,dof,expected=stats.chi2_contingency(freqtab)
    z_value=stats.chi2.ppf(q=0.95,df=2)
    print(z_value)
    if(pval>z_value):
        return pval,np.True_
    else:
        return pval,np.False_
chi_square(df)




