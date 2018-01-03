# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
import math
df = pd.read_csv('data/house_pricing.csv')

sample =df['GrLivArea']

def confidence_interval(df):

    mean=sample.mean()
    std=sample.std()
    std_error=std/math.sqrt(len(sample))
    z= stats.norm.ppf(q=0.95)
    upper_limit=float(mean+(z*std_error))
    lower_limit=float(mean-(z*std_error))
    return lower_limit,upper_limit
