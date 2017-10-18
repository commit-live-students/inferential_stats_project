# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

def chi_square(df):


    def compute_freq_chi2(x,y):
        freqtab = pd.crosstab(x,y)
        chi2,pval,dof,expected = stats.chi2_contingency(freqtab)
        return pval


    price = pd.qcut(df['SalePrice'], 3, labels = ['High', 'Medium', 'Low'])
    a=compute_freq_chi2(df.LandSlope, price)
    return a,a<0.05
