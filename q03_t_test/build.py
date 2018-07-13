# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

# Enter Code Here
def t_statistic(df):
    t_stats,pvalue=stats.ttest_1samp(a=df[df['Neighborhood']=='OldTown']['GrLivArea'], popmean=df['GrLivArea'].mean())
    test_result=pvalue < 0.05
    return pvalue,test_result
