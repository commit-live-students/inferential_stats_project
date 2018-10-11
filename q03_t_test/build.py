# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

def t_statistic(df):
    alpha=0.01
    df1=df.groupby('Neighborhood').get_group('OldTown')
    u=df['GrLivArea'].mean()
    x_bar=df1['GrLivArea'].mean()
    sigma=df['GrLivArea'].std()
    n=len(df1['Neighborhood'].values)
    z=(x_bar-u)/(sigma/(n**0.5))
    p_value=stats.norm.cdf(z)
    if p_value<alpha:
        return p_value,False
    else:
        return p_value,True


