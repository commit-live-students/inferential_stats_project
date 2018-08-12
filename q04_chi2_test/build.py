# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def chi_square(df):
    df1 = pd.qcut(x=df['SalePrice'], q=3,labels=['High', 'medium', 'low'])
    df2 = pd.crosstab(df1, df['LandSlope'])
    ans = stats.chi2_contingency(observed=df2)
    qc = stats.chi2.ppf(q=0.90, df=1)
    return ans[1], np.bool_(False)
