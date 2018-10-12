# %load q02_confidence_interval/build.py
# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']


# Write your solution here :
def confidence_interval(df):
    mean = np.mean(sample)
    stand_error = stats.sem(sample)
    print(stand_error)
    z_value = 1.96
    low_val = mean - (z_value * stand_error)
    up_val = mean + (z_value*stand_error)
    return low_val,up_val
confidence_interval(df)
a = sample
n = len(a)
m, se = np.mean(a), stats.sem(a)
print(se)
h = se * stats.t.ppf((1 + 0.90) / 2., n)
print(m-h, m+h)
import numpy as np, scipy.stats as st

st.t.interval(0.9, len(a)-1, loc=np.mean(a), scale=st.sem(a))


