import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')

def t_statistic(df):
    t_statistic, p_value = stats.ttest_1samp(a= df[df['Neighborhood'] == 'OldTown']['GrLivArea'],              
                 popmean= df['GrLivArea'].mean())
    t_critical = stats.t.ppf(1-0.1,df[df['Neighborhood'] == 'OldTown']['GrLivArea'].shape[0])
    test_result = p_value>t_critical
    
    return p_value, test_result

t_statistic(df)



