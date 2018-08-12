# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def t_statistic(df):
    statistic,p_value = stats.ttest_1samp(a=df[df['Neighborhood']=='OldTown']['GrLivArea'],popmean=df['GrLivArea'].mean())
    if p_value < 0.05:
        test_result = np.True_
    else:
        test_result = np.False_
    return p_value,test_result
