# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
import scipy.stats as stats
import math

def t_statistic(df):
    population_mean= df.GrLivArea.mean()
    population_size=len(df)
    sample = df[df.Neighborhood == 'OldTown'].GrLivArea
    sample_mean  = sample.mean()
    sample_std =sample.std()
    sample_size = sample.count()

    alpha  =1 - 0.9
    alpha_critical = alpha/2 #two sided test

    test_statistics = ( sample_mean- population_mean)/(sample_std/math.sqrt(sample_size))
    z_critical= stats.t.ppf(1-alpha_critical,(sample_size-1))

    results = stats.ttest_1samp(a= sample,               # Sample data
                 popmean= population_mean)  # Pop mean

    #Note : results.statistic matches with test_statistics: -0.65847079921234297


    p_value = results.pvalue
    test_result  = (results.pvalue > z_critical)
    return (p_value,test_result)

print t_statistic(df)
