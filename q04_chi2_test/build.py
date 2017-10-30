# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')

# Enter Code Here

def chi_square(df):
    q = pd.qcut(df.SalePrice , q=3, labels=["low", "medium", "High"])
    freqtab = pd.crosstab(index=df.LandSlope, columns=q)
    _, pvalue, __, ___ = stats.chi2_contingency(freqtab)
    significance = (1-.90) / 2

    if pvalue <= significance:
        reject_null = True
    else:
        reject_null = False

    return pvalue, np.bool_(reject_null)
