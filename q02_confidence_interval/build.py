# %load q02_confidence_interval/build.py
# Default imports
import math
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

def confidence_interval(df):
    sample = df['GrLivArea']
    sample_mean=sample.mean()
    z_value=stats.norm.ppf(0.90)
    pop_stdev=sample.std()
# Write your solution here :
    std_err=pop_stdev/math.sqrt(len(sample))
    low_limit=sample_mean-(z_value*std_err)
    upp_limit=sample_mean+(z_value*std_err)
    return float(low_limit), float(upp_limit)
