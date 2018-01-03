# Default imports
import scipy.stats as stats
import pandas as pd
import scipy.stats as sp

df = pd.read_csv('data/house_pricing.csv')

def chi_square(df):
    price = pd.qcut(df['SalePrice'], 3, labels = ['High', 'Medium', 'Low'])
    freqtab = pd.crosstab(df.LandSlope, price)
    chi2,pval,dof,expected = sp.chi2_contingency(freqtab)
    bool=pval < 0.05
    pval1=float(pval)
    return pval1,bool
