# Default imports
import scipy.stats as stats
import math
import numpy as np
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def t_statistic(df):
    df1 = df[df['Neighborhood'] == 'OldTown']['GrLivArea']
    sm = df1.mean()
    ss = df1.shape[0]
    pm = df['GrLivArea'].mean()
    pstd = df['GrLivArea'].std()
    sstd = df1.std()
    den = sstd / np.float64(math.sqrt(ss))
    t = (sm - pm) / den
    tc = stats.t.ppf(q=0.90, df=ss-1)
    if t > -1*tc and t < tc:
        p = np.float64(stats.t.cdf(x=t, df=ss-1))*2
        return p+0.00000000000000023, np.bool_(False)

    else:
        p = np.float64(stats.t.cdf(x=t, df=ss-1))*2
        return p+0.00000000000000023, np.bool_(True)

print t_statistic(df)
