# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

def chi_square(df):
    df['SalePricecat']=pd.qcut(df['SalePrice'],3,['High','Medium','Low'])
    a = pd.crosstab(df['SalePricecat'],df['LandSlope'])
    b = stats.chi2_contingency(a)
    return b[1],(b[1] < 0.05 or b[1] >0.95)#df.pivot_table(index='LandSlope',columns='SalePricecat',aggfunc='count')   #df.pivot(df['LandSlope'],df['SalePricecat'])
#     stats.
# Enter Code Here
