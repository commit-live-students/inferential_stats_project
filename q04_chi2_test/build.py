# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def chi_square(data):
    price = pd.qcut(data['SalePrice'], 3, labels = ['High', 'Medium', 'Low'])
    slope_price_freqtab = pd.crosstab(data.LandSlope, price)
    chi2, pval, dof, expected = stats.chi2_contingency(slope_price_freqtab)
    chi_test_result = pval < 0.05
    return (pval, chi_test_result)
