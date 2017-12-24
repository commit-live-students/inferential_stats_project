# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def t_statistic(data):
    teststat = stats.ttest_1samp(a=df[df['Neighborhood']=='OldTown']['GrLivArea'],popmean=df['GrLivArea'].mean()) #Q3 problem statement
    p_val = teststat[1]
    t_critic = stats.t.ppf(q=0.9,df = df[df['Neighborhood']=='OldTown']['GrLivArea'].mean())
    if p_val < t_critic:
        return p_val, np.bool_(False)
    else:
        return p_val, np.bool_(True)
