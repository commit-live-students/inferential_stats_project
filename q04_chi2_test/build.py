# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def chi_square(df):
    df['SalePrice']=pd.qcut(df['SalePrice'],3,labels=['High','Medium','low'])
    from sklearn import preprocessing
    le = preprocessing.LabelEncoder()
    df['SalePrice'] = le.fit_transform(df['SalePrice'])
    df['LandSlope'] = le.fit_transform(df['LandSlope'])
    freqtab = pd.crosstab(df['LandSlope'],df['SalePrice'])
    chi2,pval,dof,expected = stats.chi2_contingency(freqtab)
    return pval,pval<.1
