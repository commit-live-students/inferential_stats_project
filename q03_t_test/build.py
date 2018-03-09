
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

def t_statistic(df):
    t_statistic, p_value = stats.ttest_1samp(a=df[df['Neighborhood']=='OldTown']['GrLivArea'], popmean=df['GrLivArea'].mean())
    return p_value, p_value < 0.05

