# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')
# Enter Code Here
def t_statistic(df):
    old_town = df[df['Neighborhood']  == 'OldTown']['GrLivArea']
    population = df['GrLivArea']
    population_mean = population.mean()
    tstats = stats.ttest_1samp(old_town,population_mean)
    pvalue = tstats.pvalue
    reject_h = pvalue < 0.1
    return pvalue,reject_h
t_statistic(df)


