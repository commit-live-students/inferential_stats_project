# %load q04_chi2_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')

def chi_square(df):
    x=pd.qcut(df['SalePrice'],3,labels=['High','medium','low'])
    #a=pd.crosstab(index=x.values,columns='count')
    #b=pd.crosstab(index=df['LandSlope'].values,columns='count')
    a=pd.crosstab(df['LandSlope'],x)
    chi2,pval,dof,exp=stats.chi2_contingency(a)
    return pval,(pval<0.1).astype(np.bool)
#chi_square(df)
