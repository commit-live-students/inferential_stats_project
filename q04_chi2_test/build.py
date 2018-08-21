# %load q04_chi2_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

def chi_square(df):
    a=pd.qcut(df['SalePrice'],3,labels=['High','Medium','Low'])#divides  column values into three equidistant categories
    b=pd.crosstab(df['LandSlope'],a)#Gives us a count of one column values with respect to another column values.Don't put margins=True
    return stats.chi2_contingency(b)[1],stats.chi2_contingency(b)[1]<0.05
c=chi_square(df)
type(c[0])












