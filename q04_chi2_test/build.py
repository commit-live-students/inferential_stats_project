import scipy.stats as stats
import pandas as pd


df = pd.read_csv('data/house_pricing.csv')

def chi_square(df):
    lsdf = df['LandSlope']
    catdf = pd.qcut(df['SalePrice'], 3, labels = ['High','Med','Low'], retbins= False)
    freqtab=pd.crosstab(df['LandSlope'],catdf)
    chi2,p_value,dof,expected = stats.chi2_contingency(freqtab)
    test_result=(p_value<0.05)
    print(freqtab)
    
    return p_value, test_result

chi_square(df)


