# %load q02_confidence_interval/build.py
# Default imports
import math
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']
def confidence_interval(sample):
    sample_mean=sample.mean()
    #z_value=stats.norm.ppf(q=0.90)
    z_value=1.645
    pop_stdev=sample.std()
# Write your solution here :
    std_err=(pop_stdev/(math.sqrt(len(sample))))
    low_limit=sample_mean-(z_value*std_err)
    upp_limit=sample_mean+(z_value*std_err)
    return float(low_limit), float(upp_limit)
confidence_interval(sample)
