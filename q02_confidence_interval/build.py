# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']


# Write your solution here :
def confidence_interval(sample):
    confid_intrval_pct = 0.95
    # Get z score
    z_score = stats.norm.ppf(q=confid_intrval_pct)
    mean_val = sample.mean()
    margin_of_error = z_score * sample.std() / math.sqrt(sample.size)
    return (mean_val - margin_of_error,mean_val + margin_of_error)
