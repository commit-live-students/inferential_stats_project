# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np


df = pd.read_csv('data/house_pricing.csv')

def t_statistic(df):
    t_test, p_value = stats.ttest_1samp(a= df[df['Neighborhood']=='OldTown']['GrLivArea'],popmean= df['GrLivArea'].mean())
    if p_value < .1:
        result = True
    else:
        result = False
    return p_value, np.bool_(result)

# Enter Code Here
