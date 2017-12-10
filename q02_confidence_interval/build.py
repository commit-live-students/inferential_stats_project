# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']


# Write your solution here :

def confidence_interval(sample):
        sample_size = sample.shape[0]
        #print sample_size
        sample_mean = np.mean(sample)
        #print sample_mean
        sample_std = np.std(sample)
        #print sample_std
        std_error = sample_std/math.sqrt(sample_size)
        #print std_error
        z_score = 1.645
        #z_score = (sample - sample_mean)/sample_std
        #print z_score
        upper_conf = sample_mean + (z_score * std_error)
        lower_conf = sample_mean - (z_score * std_error)

        return lower_conf, upper_conf
