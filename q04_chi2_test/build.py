# Default imports
import numpy as np
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

# Enter Code Here

print df.head()

def chi_square(df):
    prices = pd.qcut(df['SalePrice'], 3, labels=["high", "medium", "low"])
    freqtab = pd.crosstab(df['LandSlope'], prices)
    chi2, p, dof, expected = stats.chi2_contingency(freqtab)
    return p, np.bool_(True if p < 0.05 else False)
