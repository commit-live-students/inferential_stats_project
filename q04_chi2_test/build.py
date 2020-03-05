# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')


def chi_square(df):
    count_LS = df.LandSlope.value_counts()
    #print count_LS
    cat_sp = pd.qcut(x= df.SalePrice , q =3 , labels=['High','Medium','Low'])
    #print cat_sp.value_counts()
    freq = pd.crosstab(df.LandSlope,cat_sp)
    #print freq
    chi2,pval,dof,expected = stats.chi2_contingency(freq)
    crit = stats.chi2.ppf(q=0.95 , df = 4)
    if chi2 < crit:
        result = np.bool_(False)
    else:
        result = np.bool_(True)

    return(pval , result)

chi_square(df)
