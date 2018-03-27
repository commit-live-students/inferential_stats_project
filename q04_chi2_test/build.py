# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
bol = np.bool_(dtype=bool)

# Enter Code Here
def chi_square(data):
    crit = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 2)
    price= pd.qcut(data['SalePrice'], 3, labels=["High","medium","Low"])
    freqtab = pd.crosstab(data['LandSlope'],price)
    chi2,pval,dof,expected = stats.chi2_contingency(freqtab)
    if chi2 > crit:
        bol = np.bool_(True)
    else:
        bol = np.bool_(False)
    return pval,bol
