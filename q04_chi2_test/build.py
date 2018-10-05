# %load q04_chi2_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')




 
# Enter Code Here
def chi_square(df):
    SalesPrice = pd.qcut(df['SalePrice'], 3, labels=['High','medium','low'])
    freqtab = pd.crosstab(df['LandSlope'],SalesPrice)
    chi,p_value,dof,expected = stats.chi2_contingency(freqtab)
    
    if p_value < 0.05:
        test_result = np.True_
    else:
        test_result = np.False_
    
    return p_value, test_result
    
chi_square(df)



#def chisq_of_df_cols(df, c1, c2):
#     groupsizes = df.groupby([c1, c2]).size()
#     ctsum=pandas.crosstab(index=test_df['var1'],columns=test_df['var2'])
#     # fillna(0) is necessary to remove any NAs which will cause exceptions
#     return(chi2_contingency(ctsum.fillna(0)))

# test_df = pandas.DataFrame([[0, 1], [1, 0], [0, 2], [0, 1], [0, 2]], columns=['var1', 'var2'])
# chisq_of_df_cols(test_df, 'var1', 'var



