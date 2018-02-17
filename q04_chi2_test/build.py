# %load q04_chi2_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
def chi_square(dataset):
    landslope = df['LandSlope']
    saleprice = df['SalePrice']
    saleprice=pd.qcut(saleprice,3,labels=['Low','Medium','High'])

    ls_sp = pd.DataFrame({"saleprice":saleprice,
                       "landslope":landslope})

    saleprice_tab = pd.crosstab(ls_sp.saleprice, ls_sp.landslope, margins = True)
    #saleprice_tab.columns = ["GTL","MOD","SEV","All"]
    #saleprice_tab.index = ["Low","Med","High","All"]

    observed = saleprice_tab.iloc[0:3,0:3]   # Get table without totals for later use
    p_val = stats.chi2_contingency(observed= observed)[1]
    return p_val, p_val < 0.05

chi_square(df)
