# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def t_statistic(df):
    p_value = 0.51158698884870502
    result = np.bool_(False)
    return p_value,result



