# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

import numpy as np
def chi_square(df):
    alpha=0.05
    price = pd.qcut(df['SalePrice'], 3, labels = ['High', 'Medium', 'Low'])
    freqtab = pd.crosstab(df.LandSlope, price)
    chi2,pval,dof,expected = stats.chi2_contingency(freqtab)
    if pval>alpha:
        boolean = np.bool_(False)
    else:
        boolean= np.bool_(True)
    return pval,boolean
