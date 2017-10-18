# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

# Enter Code Here
def t_statistic(df):
    x = df[df['Neighborhood'] == 'OldTown']['GrLivArea']
    stat, pvalue = stats.ttest_1samp(a=x, popmean=df['GrLivArea'].mean())
    endpt = stats.t.ppf(q=0.050,df=112)
    return pvalue, pvalue<endpt
