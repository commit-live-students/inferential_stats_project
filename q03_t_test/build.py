# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')

def t_statistic(df):
    k = stats.ttest_1samp(a = df[df['Neighborhood'] == 'OldTown']['GrLivArea'] , popmean = df['GrLivArea'].mean())
    k.pvalue

    if k.pvalue > 0.90:
        test_result = np.bool_(True)
    else:
        test_result = np.bool_(False)
    #print type(test_result)
    return (k.pvalue , test_result)

t_statistic(df)
