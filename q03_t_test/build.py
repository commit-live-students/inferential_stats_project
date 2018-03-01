# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')

def t_statistic(df):

    t_statistic, p_value  = stats.ttest_1samp(df[df['Neighborhood'] \
                                              == 'OldTown']['GrLivArea'], \
                                              df['GrLivArea'].mean())

    # If pval > alpha, the hypothesis is never rejected
    if (p_value > 0.1):
        test_result = np.bool_(False)
    else :
        test_result = np.bool_(True)

    return p_value, test_result
