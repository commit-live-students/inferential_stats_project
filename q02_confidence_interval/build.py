# Default imports
import math
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']

def confidence_interval(sample):
    N = sample.shape[0]
    sample_mean = sample.mean()
    sample_std = sample.std()
    z_score = 1.645
    estimated_error = z_score * (sample_std/math.sqrt(N))
    lwr_lmt_cnf_intrvl = sample_mean - estimated_error
    upr_lmt_cnf_intrvl = sample_mean + estimated_error
    return lwr_lmt_cnf_intrvl,upr_lmt_cnf_intrvl
# Write your solution here :
