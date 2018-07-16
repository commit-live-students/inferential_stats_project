# Default imports
from __future__ import division
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')

def t_statistic(df):
    #Ho : mean(old_town) = mean(population)
    p_value = stats.ttest_1samp(df[df['Neighborhood']=='OldTown']['GrLivArea'],df['GrLivArea'].mean()).pvalue
    exp_pval = stats.t.ppf(q=0.90,df=49)
    if(p_value < exp_pval):
        return p_value,np.bool_(False)
    else :
        return p_value,np.bool_(True)
