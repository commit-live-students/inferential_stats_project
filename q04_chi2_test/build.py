# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

# Enter Code Here
def chi_square(df):
    q = pd.qcut(df.SalePrice , q=3)
    print q
    #return p_value, test_result


print chi_square(df)
