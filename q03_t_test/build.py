# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')

def t_statistic(df):
    x=stats.ttest_1samp(a=df[df['Neighborhood']=='OldTown']['GrLivArea'],popmean=df['GrLivArea'].mean())

    return x[1],(x[1]<0.1).astype(np.bool)
#type(t_statistic(df)[1])
