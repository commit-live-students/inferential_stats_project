# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

def t_statistic(df):
    alpha=0.05
    fil1=df['Neighborhood']=='OldTown'
    newdf=df.loc[fil1,'GrLivArea']
    s,p_value=stats.ttest_1samp(newdf,df.loc[:,'GrLivArea'].mean())
    result=p_value<alpha
    return p_value,result

# Enter Code Here
