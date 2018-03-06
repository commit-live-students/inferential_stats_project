# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')

def t_statistic(df):
    alpha=0.10
    stats_1 = stats.ttest_1samp(a= df[df['Neighborhood'] == 'OldTown']['GrLivArea'], popmean= df['GrLivArea'].mean())
    if stats_1.pvalue > alpha:
        boolean = np.bool_(False)
    else:
        boolean = np.bool_(True)

    return (stats_1.pvalue,(boolean))
