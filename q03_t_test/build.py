# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def t_statistic(df):

    test_value, p_value = stats.ttest_1samp(df[df.Neighborhood =='OldTown']['GrLivArea'], popmean = df['GrLivArea'].mean())
    test_result=p_value<0.1
    return p_value, test_result
print t_statistic(df)
