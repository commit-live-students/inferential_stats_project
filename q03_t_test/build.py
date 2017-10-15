# %load q03_t_test/build.py
# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')
#print(df.info())

# Enter Code Here
def t_statistic(df):
    liv_area_old_town=df[df['Neighborhood']=='OldTown']['GrLivArea']
    liv_area_old_town_mean = liv_area_old_town.mean()
    #print(liv_area_old_town_mean)
    liv_area_mean=df['GrLivArea'].mean()
    #print(liv_area_mean)
    noOfSample=len(liv_area_old_town)
    #print(noOfSample)
    statistic, p_value =stats.ttest_1samp(a=liv_area_old_town,popmean=liv_area_mean)
    #print(type(p_value.item()))
    # for 90% significane level c=0.1
    if(p_value.item()<0.1):
        #we reject null hypothesis
        return p_value.item(),np.False_
    else:
        # we don't reject null hypotheses
        return p_value.item(), np.False_
