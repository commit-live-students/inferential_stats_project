# %load q02_confidence_interval/build.py
# Default imports
import math
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']


# Write your solution here :
def confidence_interval(sample):
    #np.random.seed(5)
    n=sample.shape[0]
    z= stats.norm.ppf(q = 0.95)
    s=sample.std()
    #s=df['GrLivArea'].std()
    mean=sample.mean()
    se=s/math.sqrt(n)
    est=z*se
    low=mean-est
    high=mean+est
    return low,high

confidence_interval(sample)
