# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def chi_square(data):
    value = pd.qcut(data['SalePrice'],3, labels = ['High', 'Medium', 'Low'])
# compute_freq_chi2(data.LandContour, value)
    freqtab = pd.crosstab(data.LandSlope,value)
    # print freqtab
    chi2,pval,dof,expected = stats.chi2_contingency(freqtab)
    test_result = chi2 > 5
    return float(pval), test_result

# print chi_square(df)
