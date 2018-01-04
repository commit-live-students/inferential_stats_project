# %load q04_chi2_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
from statsmodels.stats.weightstats import ztest
import numpy as np
def chi_square(df):
    # Check chi square
    # Create a new column for categorization of Sale Price
    df["SPCat"] = pd.qcut(df["SalePrice"], 3, labels=["High", "Medium", "Low"])

    # Create frequency table
    freqtab = pd.crosstab(df["LandSlope"], df["SPCat"])

#     print ("Frequency Table")
#     print ("---------------")
#     print freqtab

    # Do the chi-square test
    chi2,pval,dof,expected = stats.chi2_contingency(freqtab)

#     print ("Chi-square Test")
#     print ("---------------")
#     print ("ChiSquare test statistic: ",chi2)
#     print ("p-value: ",pval)

    # Assume steady state as H0 as True
    test_result = np.bool_(True)
    if pval > 0.05:
        test_result = np.bool_(False)

#     print ("Hypothesis Result")
#     print ("-----------------")
#     print H0

    # Voila
    return pval.item(), test_result

p,h = chi_square(df)
print p
print h
print type(p)
print type(h)
