# Need to check this.  This is wrong I guess.
# %load q04_chi2_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def chi_square(df):
      
    # Find the critical value for 95% confidence*
    # Df = number of variable categories - 1    
    crit = stats.chi2.ppf(q = 0.95,df = 2) 
    #print('Critical value            : ',crit)
    
    x = df['LandSlope']
    y = pd.qcut(df['SalePrice'],3,labels=['High', 'medium', 'low'])
    
    freqtab = pd.crosstab(x,y)
    chi2,pval,dof,expected = stats.chi2_contingency(freqtab)
    
    #print('Chi-square test statistic : ',chi2)
    #print('P-Value                   : ',pval)
    
    # If chi-square value exceeds critical value, reject the Null hypothesis viz. return False
    return pval,(chi2>crit)
    
    

    
#Call to the function -
chi_square(df)



