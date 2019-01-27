# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here

def t_statistic(df):
    population = df['GrLivArea']
    sample = df[df['Neighborhood'] == 'OldTown']['GrLivArea']
        
    statistic, p_value = stats.ttest_1samp(sample, popmean= population.mean())

    nullHypothesisIsCorrect = np.greater(p_value, 0.9)
        
    return p_value, nullHypothesisIsCorrect
t_statistic(df)


