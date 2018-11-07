# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def t_statistic(df):
    zstat,pval=stats.ttest_1samp(df[df['Neighborhood']=='OldTown']['GrLivArea'],df['GrLivArea'].mean())
    return(pval,(pval<0.1))

t_statistic(df)

