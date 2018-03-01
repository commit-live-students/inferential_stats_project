# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
import numpy as np
def chi_square(df):
    q = pd.qcut(df.SalePrice , q=3, labels=["low", "medium", "High"])
    freqtab = pd.crosstab(index=df.LandSlope, columns=q)
    chiSquare_test_statistic, p_value, degree_of_freedom, expected = stats.chi2_contingency(freqtab)
    significance = (1-.90) / 2 # # 95% significance level. Two-way t-test => .05/ 2 = .025

    if p_value <= significance:
        reject_null = True
    else:
        reject_null = False

    return p_value, np.bool_(reject_null)
