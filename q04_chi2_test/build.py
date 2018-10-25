# %load q04_chi2_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def chi_square(df):
    '''Function to test the independence of two variables
    H0: The variables are independent
    HA: The variables are dependent
    
    significance = 0.05
    '''
    
    #using qcut to divide Salesprice in categorical lables
    df['SalesCat'] = pd.qcut(x=df['SalePrice'],labels=['Low','Medium','High'],q=3)
    
    #This table is the observed table
    cont = pd.crosstab(df['SalesCat'],df['LandSlope'])
    
    #Run chi2 test by running contigency test
    chi_stat, p_value , dof, arr = stats.chi2_contingency(cont)
    
    if p_value < 0.05:
        test_result = np.bool_(True)
    else:
        test_result = np.bool_(False)
    return p_value, test_result

chi_square(df)





