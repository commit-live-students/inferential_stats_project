# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def t_statistic(df):
    t_statistic,p_value=stats.ttest_1samp(a= df[df['Neighborhood'] == 'OldTown']['GrLivArea'],popmean= df['GrLivArea'].mean())

    if (p_value<0.9):
        flag=np.bool_(False)
    else:
        flag=np.bool_(True)
    return p_value,flag
