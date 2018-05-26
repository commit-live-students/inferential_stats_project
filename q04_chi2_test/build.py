# %load q04_chi2_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def compute_freq_chi2(x,y):
    freqtab = pd.crosstab(x,y)
    chi2, pval, dof, expected = stats.chi2_contingency(freqtab)
    return pval

def chi_square(df):
    price = pd.qcut(df['SalePrice'],3,labels = ['High', 'Medium','Low'])
    pval =  compute_freq_chi2(df.LandSlope, price)
    crit = stats.chi2.ppf(q=0.95, df=2)
    
    if (pval<crit):
        return pval, np.False_
    else:
        return pval, np.True_
    
chi_square(df)
    



