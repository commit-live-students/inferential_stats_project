# Default imports
import scipy.stats as stats
import pandas as pd
from statsmodels.stats.weightstats import ztest

df = pd.read_csv('data/house_pricing.csv')
def t_statistic(df):
    a,b = stats.ttest_1samp(a= df[df['Neighborhood'] == 'OldTown']['GrLivArea'],popmean= df['GrLivArea'].mean())
    return b,b<0.025




# Enter Code Here
