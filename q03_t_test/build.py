# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd

data = pd.read_csv('data/house_pricing.csv')

def t_statistic(data):
    t_statistic, p_value = stats.ttest_1samp(a= data[data['Neighborhood'] == 'OldTown']['GrLivArea'], popmean= data['GrLivArea'].mean())  # Pop mean
    return float(p_value), p_value < 0.05

#print t_statistic(data)

