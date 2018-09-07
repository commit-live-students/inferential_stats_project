# %load q04_chi2_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def chi_square(df):
    
    def compute_freq_chi2(x,y):
        freqtab = pd.crosstab(x,y)
        chi2,pval,dof,expected = stats.chi2_contingency(freqtab)
        return pval, pval<0.05
    price = pd.qcut(df['SalePrice'], 3, labels = ['High', 'Medium', 'Low'])
    return compute_freq_chi2(df.LandSlope, price)
chi_square(df)



