# %load q02_confidence_interval/build.py
# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']
def confidence_interval(sample): 
    sample_data=np.random.choice(a=df['GrLivArea'],size=1460)
    z_critical=stats.norm.ppf(0.95)
    sigma=sample.std()
    sample_mean=sample.mean()
    SE=sigma/math.sqrt(1460)
    estimate=z_critical*SE
    confidence_interval=(sample_mean-estimate,sample_mean+estimate)
    return(confidence_interval)

confidence_interval(sample)

