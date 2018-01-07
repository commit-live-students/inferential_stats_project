# Default imports
import scipy.stats as sp
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def chi_square(data):
    """This function will compute frequency table of x an y
    Pandas Series, and use the table to feed for the contigency table

    Parameters:
    -------
    x,y : Pandas Series, must be same shape for frequency table

    Return:
    -------
    None. But prints out frequency table, chi2 test statistic, and
    p-value
    """
    price = pd.qcut(df['SalePrice'], 3, labels = ['High', 'Medium', 'Low'])
    freqtab = pd.crosstab(df.LandSlope, price)
    print("Frequency table")
    print("============================")
    print(freqtab)
    print("============================")
    chi2,pval,dof,expected = sp.chi2_contingency(freqtab)
    test_result=pval>0.5
    print("ChiSquare test statistic: ",chi2)
    print("p-value: ",pval)
    return pval,test_result
