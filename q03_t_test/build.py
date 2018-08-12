# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')
def t_statistic(df):
    import numpy as np
    tstat, p_value = stats.ttest_1samp(a = df[df['Neighborhood']=='OldTown']['GrLivArea'],popmean = df['GrLivArea'].mean())
    if p_value < 0.05:
        test_result = np.True_
    else:
        test_result = np.False_
    return p_value,test_result
