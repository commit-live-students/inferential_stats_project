# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
# df = pd.read_csv('data/house_pricing.csv')
# data = df
# print df['GrLivArea'].describe()
# print df[df['Neighborhood']=='OldTown']['GrLivArea'].describe()

def t_statistic(data):
    z_stats,p_value=stats.ttest_1samp(a= data[data['Neighborhood'] == 'OldTown']['GrLivArea'],popmean= data['GrLivArea'].mean())
    print ('Z-statistic :{}'.format(z_stats))
    print ('p-value :{}'.format(p_value))
    return z_stats > 1.645, p_value
print t_statistic(df)
