# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def chi_square(df):

    x = df.LandSlope
    price = pd.qcut(df['SalePrice'],3,labels = ['High','Medium','Low'])
    freqtab = pd.crosstab(x,price)
    chi2,pval,dof,expected = stats.chi2_contingency(freqtab)
    chi_test = np.bool_(False)
    #print type(chi_test)
    #print freqtab
    return pval,chi_test

print chi_square(df)
