# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def t_statistic(df):
    
    t_statistic,p_value = stats.ttest_1samp(a= df[df['Neighborhood']=='OldTown']['GrLivArea'],               # Sample data
                 popmean= df['GrLivArea'].mean())  # Pop mean
    return p_value,p_value<0.05
    

