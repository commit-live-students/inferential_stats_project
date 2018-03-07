import numpy as np
import scipy.stats as stats
import pandas as pd
#from statsmodels.stats.weightstats import ztest

df = pd.read_csv('data/house_pricing.csv')

def t_statistic(df):
    pop_mean = df['GrLivArea'].mean()
    N=df[df['Neighborhood'] == 'OldTown']['GrLivArea']
    N_mean = N.mean()
    t_test = stats.ttest_1samp(N,pop_mean)
    p_value=t_test[1]
    alpha= (p_value*90)/100
    test_result = np.less(p_value,alpha)
    return p_value,test_result
