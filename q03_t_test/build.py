# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def t_statistic(df):
    # H0 => mean_liv_area_oldTown = mean_liv_area_pop
    # H1 => mean_liv_area_oldTown != mean_liv_area_pop
    # significance level 90%
    old_town_data = df[df['Neighborhood'] == 'OldTown']['GrLivArea']
    pop_mean = df['GrLivArea'].mean()
    results = stats.ttest_1samp(a=old_town_data,popmean=pop_mean)
    pvalue = results.pvalue
    test_result = results.statistic
    reject_h0 = pvalue < 0.1
    return pvalue, reject_h0

t_statistic(df)


