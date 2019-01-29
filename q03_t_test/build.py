# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
from statsmodels.stats.weightstats import ztest

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here


#def t_statistic(df=df):
 #   mean_liv_area = df['GrLivArea'].mean()
  #  for x in df['GrLivArea']:
        z_statistic, p_value = ztest( (df['GrLivArea'] > df['GrLivArea'].mean()) | (df['GrLivArea'] < df['GrLivArea'].mean()),
            value=df['GrLivArea'].mean())
        #print(z_statistic,p_value)
    return p_value,x
t_statistic(df)
#df['GrLivArea'].mean()


