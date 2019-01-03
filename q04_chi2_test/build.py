# %load q04_chi2_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def chi_square(df):
    
    #price converted into catogrical on basic of quantile
    price = pd.qcut(df['SalePrice'],3, labels =['low', 'medium', 'High'])
    
    #contingency table group variable to show correlation between two varable
    freq_table = pd.crosstab(df.LandSlope, price)
    
    #calculting chi and p value from 
    chi, p, dof, expected = stats.chi2_contingency(freq_table)
    
    if p < 0.05: # if value of p is very low than variable are independent
        return p, np.bool_(True)
    else:
        return p, np.bool_(False) #else not independent



chi_square(df)


