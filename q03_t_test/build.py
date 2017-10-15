# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')

# Enter Code Here
def t_statistic(df):
    res = stats.ttest_1samp(a= df[df['Neighborhood'] == 'OldTown']['GrLivArea'],popmean= df['GrLivArea'].mean())
    p_value = res[1]
    if p_value < 0.1:
        test_result = True
    else:
        test_result = False

    return float(p_value),np.bool_(test_result)
