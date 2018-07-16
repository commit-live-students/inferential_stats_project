import numpy as np
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

def chi_square(df):
    SalePrice_Category = pd.qcut(df['SalePrice'], 3, labels=["High", "Medium", "Low"])
    freqtab = pd.crosstab(SalePrice_Category,df['LandSlope'])
    print("Frequency table")
    print("============================")
    print(freqtab)

    chi2,pval,dof,expected = stats.chi2_contingency(freqtab)
    print("Degree of Freedom:",dof)
    print("ChiSquare test statistic: ",chi2)
    print("p-value: ",pval)
    test_result = np.greater(pval,chi2)
    return pval,test_result

print chi_square(df)
