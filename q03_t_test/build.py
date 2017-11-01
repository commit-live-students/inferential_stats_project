# Default imports
import numpy as np
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

# Enter Code Here

def t_statistic(df):
    _, p = stats.ttest_1samp(a=df[df['Neighborhood'] == 'OldTown']['GrLivArea'],
                             popmean=df['GrLivArea'].mean())

    return p, np.bool_(True if p < 0.5 else False)
