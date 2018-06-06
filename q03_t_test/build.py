# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
# Enter Code Here
def t_statistic(df):
    live_area = df['GrLivArea']
    oldtown_area = df['GrLivArea'][df['Neighborhood']=='OldTown']
    live_area_mean = live_area.mean()
    oldtown_area_mean = oldtown_area.mean()
    z_cricitcal = stats.norm.ppf(q=0.90)
    tstat,pvalue = stats.ttest_1samp(oldtown_area,live_area_mean)

    #print('z critical: ',z_cricitcal)
    #print('Total Living area mean: ',live_area_mean)
    #print('Oldtown living area mean: ',oldtown_area_mean)
    #print('P Value: ',pvalue)

    if(pvalue < z_cricitcal):
        test_result = np.bool_(False)
        #print('We reject null hypothesis')
    else:
        test_result = True
        #print('We fail to reject null hypothesis')
    return float(pvalue),test_result
#(t_statistic(df))


