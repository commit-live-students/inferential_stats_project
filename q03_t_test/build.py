# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def t_statistic(data):
    
    zstats,pvalue=stats.ttest_1samp(a= data[data['Neighborhood'] == 'OldTown']['GrLivArea'],popmean= data['GrLivArea'].mean()) 
    zstats=np.bool_(True) if(zstats>0) else np.bool_(False)
    return pvalue,zstats



