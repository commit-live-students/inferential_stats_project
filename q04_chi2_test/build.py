# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
# https://www.youtube.com/watch?v=misMgRRV3jQ

def chi_square(df):
    series1 = df.LandSlope
    series2 = pd.qcut(df.SalePrice,3,labels=["low","medium","High"])
    freqtable= pd.crosstab(series1,series2)
    chi2,p_value,dof,expected = stats.chi2_contingency(freqtable)
    chi_critical = stats.chi.ppf(q=0.95, df=dof)
    test_result = (chi2< chi_critical)
    return(p_value,test_result)

#print (chi_square(df))
