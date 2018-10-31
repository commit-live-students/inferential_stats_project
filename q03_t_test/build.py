# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest

df = pd.read_csv('data/house_pricing.csv')
sample = np.random.choice(a = df['GrLivArea'], size = 500)

# Enter Code Here
def t_statistic(df):
    sample_mean = sample.mean()
    t_statistic, p_value = stats.ttest_1samp(a = df[df['Neighborhood'] == 'OldTown']['GrLivArea'],
    popmean = df['GrLivArea'].mean())
    return p_value, p_value < 0.05

t_statistic(df)    


