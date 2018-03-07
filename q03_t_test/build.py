# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

data = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def t_statistic(data):
    t, p_value = stats.ttest_1samp(a= data[data['Neighborhood'] == 'OldTown']['GrLivArea'],               # Sample data
                 popmean= data['GrLivArea'].mean())

    if p_value < 10:
        return p_value, np.bool_(False)



print t_statistic(data)
