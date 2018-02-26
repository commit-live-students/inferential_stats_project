# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

def chi_square(df):
    import numpy as np
    price = pd.qcut(df['SalePrice'],3,labels = ['High','Medium','Low'])
    freqtab = pd.crosstab(df.LandSlope,price)
    chi2,pval,dof,expected = stats.chi2_contingency(freqtab)

    if pval < 0.05:
        result = np.True_
    else:
        result = np.False_

    return pval, result

print chi_square(df)
# Enter Code Here
