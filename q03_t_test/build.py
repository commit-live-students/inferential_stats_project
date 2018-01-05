import scipy.stats as stats
import pandas as pd
from statsmodels.stats.weightstats import ztest


data = pd.read_csv('data/house_pricing.csv')
def t_statistic(df):
    statistic, p_value=stats.ttest_1samp(a= data[data['Neighborhood'] == 'OldTown']['GrLivArea'],
                 popmean= data['GrLivArea'].mean())


    bool=p_value < 0.10
    pval=float(p_value)
    return pval,bool
