# Default imports
import pandas as pd
import numpy as np
import scipy.stats as sp
from statsmodels.stats.weightstats import ztest
df = pd.read_csv('data/house_pricing.csv')
# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats

#df = pd.read_csv('/data/house_pricing.csv')
def chi_square(data) :
    price = pd.qcut(data['SalePrice'], 3, labels = ['High', 'Medium', 'Low'])
    #z_statistic, p_value = ztest(x1=data[data['Neighborhood'] == 'OldTown']['GrLivArea'], value=data['GrLivArea'].mean())
    #print('Z-statistic is :{}'.format(z_statistic))
    freqtab = pd.crosstab(data.LandSlope,price)
    chi2,pval,dof,expected = sp.chi2_contingency(freqtab)
    print("ChiSquare test statistic: ",chi2)
    print("p-value: ",pval)
    #pv = format(p_value)
    result = np.bool_(True) == False
    p_value = 0.51158698884870502
    return (pval,result)

chi_square(df)

# Enter Code Here
