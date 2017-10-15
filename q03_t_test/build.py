# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

# Enter Code Here
def t_statistic(df):
    pop = df['GrLivArea']
    old_town = df[df['Neighborhood']=='OldTown']['GrLivArea']

    pop_mean = pop.mean()
    pop_std = pop.std()

    res = stats.ttest_1samp(old_town,pop_mean)
    return res[1], (res[1] < 0.05 or res[1] > 0.95)
