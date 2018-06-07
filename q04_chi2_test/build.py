# %load q04_chi2_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')
# Enter Code Here
def chi_square(df):
    landslope = df['LandSlope']
    salePrice = pd.qcut(df['SalePrice'],3, labels = ['High', 'Medium', 'Low'])

    freetab = pd.crosstab(landslope,salePrice)
    print(freetab)
    chi2,pval,dof, expected = stats.chi2_contingency(freetab)
    print('Chi test stats: ',chi2)
    print('P Value: ',pval)
    #print(expected)
    if(pval < 0.05):
        test_result = True
    else:
        test_result = False
        
    return float(pval),np.bool_(test_result)

#chi_square(df)

