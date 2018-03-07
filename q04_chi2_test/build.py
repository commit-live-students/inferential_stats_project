# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def chi_square(df):
    cat_salePrice = pd.qcut(df['SalePrice'], 3, labels = ['Low', 'Medium', 'High'])
    freqtab = pd.crosstab(df.LandSlope ,cat_salePrice)
    chi2,pval,dof,expected = stats.chi2_contingency(freqtab)
    if pval < 10:
        return pval, np.bool_(False)
print chi_square(df)
