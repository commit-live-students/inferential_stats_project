
import math
import numpy as np
import scipy.stats as stats

from greyatomlib import pandas_project as pd

df = pd.read_csv('data/house_pricing.csv')
sample = np.random.choice(a=df['GrLivArea'], size=500)
def confidence_interval(sample=sample):
    sample_mean = sample.mean()
    z_critical = stats.norm.ppf(q=0.95)
    stdev = sample.std()
    standard_error = z_critical * (stdev / math.sqrt(sample.shape[0]))
    confidence_interval = (sample_mean - standard_error, sample_mean + standard_error)
    return confidence_interval

