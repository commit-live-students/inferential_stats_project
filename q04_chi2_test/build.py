# %load q04_chi2_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')

# Enter Code Here
def chi_square(data):
    #data=df
    price = pd.qcut(data['SalePrice'], 3, labels = ['High', 'Medium', 'Low'])
    #print(price)
    landSlope = data['LandSlope']
    #print(landSlope)
    freqtable= pd.crosstab(landSlope,price)
    #print(freqtable)
    chi2,pval,dof,expected = stats.chi2_contingency(freqtable)
    if(pval<0.05):
        #low p value refers that variable are dependent
        return pval.item(), np.True_
    else:
        return pval.item(),np.False_
    #return pval.item(),chi2

#chi_square(df)
