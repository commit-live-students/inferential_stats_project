# Default imports
import scipy.stats
import scipy
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']

def confidence_interval(data, confidence = 0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t._ppf((1 + confidence)/ 2., n-1)
    return m-h, m+h
