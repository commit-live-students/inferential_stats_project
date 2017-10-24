# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')

# Enter Code Here
def t_statistic(df):
    tstat,pval = stats.ttest_1samp(a=df[df['Neighborhood'] == 'OldTown']['GrLivArea'],popmean= df['GrLivArea'].mean())
    if pval < 0.05:
        return pval,np.True_
    else:
        return pval,np.False_

pval, result = t_statistic(df)
