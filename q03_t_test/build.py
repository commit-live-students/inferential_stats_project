# Default imports
import scipy.stats as stats
import pandas as pd
import numpy as np

df = pd.read_csv('data/house_pricing.csv')

# Enter Code Here
def t_statistic(df):
    t_statistic, p_val  = stats.ttest_1samp(a=df[df['Neighborhood'] == 'OldTown']['GrLivArea'], popmean=df['GrLivArea'].mean())

    alpha_level = .90
    significance_level = (1 - alpha_level) / 2  # 90% significance level. Two-way t-test => .10/ 2 = .05

    # When a P value is less than or equal to the significance level, you reject the null hypothesis
    if p_val <= significance_level :
        # Reject null
        reject_null = True
    else:
        # Do not reject null
        reject_null = False

    return p_val, np.bool_(reject_null) #np.bool_(not reject_null)
