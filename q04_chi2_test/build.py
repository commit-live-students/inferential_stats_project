# %load q04_chi2_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import scipy.stats as sp
import numpy as np
df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here

def chi_square(data):
    price = pd.qcut(data['SalePrice'], 3, labels = ['High', 'Medium', 'Low'])
    freqtab = pd.crosstab(data.LandSlope, price)
    chi2,pval,dof,expected = sp.chi2_contingency(freqtab)
    boo=np.bool_(False)
    if(pval < 0.05):
        boo= np.bool_(True)
    return pval,boo

chi_square(df)

