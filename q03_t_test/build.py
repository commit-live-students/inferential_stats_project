# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
import numpy as np
def t_statistic(df):
    t,p = stats.ttest_1samp(a= df[df['Neighborhood'] == 'OldTown']['GrLivArea'],               # Sample data
                 popmean = df['GrLivArea'].mean())  # Pop mean
    bl = np.bool_(True)
    if p >= 0.05:
        bl = np.bool_(False)
    return p.item(), bl
