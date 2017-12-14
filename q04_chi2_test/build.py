# Default imports
import scipy.stats as sp
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

import numpy as np
def chi_square(df):
    price = pd.qcut(df['SalePrice'], 3, labels = ['High', 'Medium', 'Low'])
    freqtab=pd.crosstab(df['LandSlope'],price)
    chi2,pval,dof,expected = sp.chi2_contingency(freqtab)
    if(pval<0.05):
        flag=np.bool_(True)
    else:
        flag=np.bool_(False)
    return pval,flag
# Enter Code Here
