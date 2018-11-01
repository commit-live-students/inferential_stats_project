# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')

def t_statistic(df):
    # Enter Code Here
    # alpha 0.05 for 95% significance level, its means 5% risk 
    # alpha 0.10 for 90% significance level, its means 10% risk
    alpha = 0.10
    t_test, p_value = stats.ttest_1samp(df[df['Neighborhood' ]=='OldTown']['GrLivArea'], df['GrLivArea'].mean())
    if p_value < alpha:
        return  p_value, np.bool_(False)
    
    else:
        
        return  p_value, np.bool_(True)


type(t_statistic(df)[1])
np.bool(False)
type(np.bool(False))
type(np.bool_(False))




