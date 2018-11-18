# %load q04_chi2_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def chi_square(df):
    
    df['SalePriceLabel']= pd.qcut(df.SalePrice, 3, labels=['good', 'medium', 'bad'])
    
    crosstab = pd.crosstab(df['LandSlope'],df['SalePriceLabel'])
    
    chi = stats.chi2_contingency(crosstab)[0]
    
    p_val = stats.chi2_contingency(crosstab)[1]
    
    def_of_free = stats.chi2_contingency(crosstab)[2]
    
    arr = stats.chi2_contingency(crosstab)[3]
    
    return p_val,np.bool_(np.all(arr > 5))






