# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here

def chi_square(df):
    price = pd.qcut(df['SalePrice'], 3, labels = ['High', 'Medium', 'Low'])
    freqtab = pd.crosstab(price, df.LandSlope)
    chi2,pval,dof,expected = stats.chi2_contingency(freqtab)
    crit = stats.chi2.ppf(q = 0.90,df = (freqtab.shape[0]-1)*(freqtab.shape[1]-1))
    return pval,np.bool_(True) if chi2 > crit else np.bool_(False)
