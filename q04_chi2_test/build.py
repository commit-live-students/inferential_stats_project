# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')

def compute_freq_chi2(x,y):
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
    freqtab = pd.crosstab(x,y)
    #print("Frequency table")
    #print("============================")
    #print(freqtab)
    #print("============================")

    #print("ChiSquare test statistic: ",chi2)
    #print("p-value: ",pval)
    return chi2, pval


def chi_square(df):

    sale_prcie = df['SalePrice']

    # Divide SalePrice into categories
    sale_price_cat = pd.qcut(sale_prcie, 3, labels = ["High", "Medium", "Low"])

    # ChiSquare Test
    freqtab = pd.crosstab(df.LandSlope, sale_price_cat)
    chi2,pval,dof,expected = stats.chi2_contingency(freqtab)

    # Calculate critical chi square
    chi_square_critical = stats.chi2.ppf(q = 0.05, df = 4)

    # Condition to accept/ reject hypothesis
    if chi2 < chi_square_critical:
        test_result = np.bool_(True)
    else:
        test_result = np.bool_(False)

    return pval, test_result
