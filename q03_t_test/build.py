# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def t_statistic(df):
    p_critical = stats.norm.cdf(stats.norm.ppf(q = 0.9))
    a = stats.ttest_1samp(a= df[df['Neighborhood'] == 'OldTown']['GrLivArea'],
                 popmean= df['GrLivArea'].mean())
    p_value = a[1]

    return p_value, np.bool_(True) if p_value > p_critical else np.bool_(False)
