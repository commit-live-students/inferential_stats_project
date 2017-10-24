# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

# Enter Code Here

def chi_square(df):
    SalesPrice = df.SalePrice
    LandSlope = df.LandSlope
    df_SalesPrice = pd.qcut(SalesPrice,q=3,labels = ['High', 'Medium', 'Low'])
    freqtab = pd.crosstab(LandSlope,df_SalesPrice)
    chi2,pval,dof,expected = stats.chi2_contingency(freqtab)
    result = False
    if pval < 0.05:
        result = True
    return pval,result

chi_square(df)
