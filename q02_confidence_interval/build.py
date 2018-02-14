# Default imports
import math
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']

def confidence_interval(sample):
    sd = sample.std()
    se = sd/math.sqrt(len(sample))
    mean = sample.mean()
    lcl, ucl =  mean - 1.64485362695*se , mean + 1.64485362695*se
    return lcl, ucl

# Write your solution here :
confidence_interval(sample)
# Write your solution here :
