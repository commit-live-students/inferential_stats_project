# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


def t_statistic(df):

    a = df[df['Neighborhood'] == 'OldTown']['GrLivArea']
    popmean = df['GrLivArea'].mean()

    test = stats.ttest_1samp(a,popmean)
    return test[1], test[1] < 0.05
