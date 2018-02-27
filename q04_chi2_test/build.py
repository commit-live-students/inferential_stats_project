# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')
def chi_square(df):
    df['SalePrice_cat']=pd.qcut(df['SalePrice'],3,labels=["low", "medium", "high"])
    x = df['SalePrice_cat']
    y = df['LandSlope']
    freqtab = pd.crosstab(x,y)
    print("Frequency table")
    chi2,pval,dof,expected = stats.chi2_contingency(freqtab)
    if pval>=0.05:
        result = np.bool_(False)
    else:
        result = np.bool_(True)
    return pval,result





# Enter Code Here
