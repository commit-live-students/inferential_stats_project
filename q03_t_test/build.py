# Default imports
import scipy.stats as stats
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def t_statistic(data):
    # considering two tailed t-test and confidence interval given is 90%
    # as we are trying with null hypothesis of
    # "The mean of Living area of houses in OldTown is the same as the population mean"
    exp_p_value = (1 - 0.9) / 2
    gr_livng_area = df['GrLivArea']
    # Get the mean of the population
    pop_mean = gr_livng_area.mean()
    # Get OldTown's GrLivArea data as Sample
    gr_livng_area_sample = df[df['Neighborhood']=='OldTown'].GrLivArea
    p_value = stats.ttest_1samp(a=gr_livng_area_sample,popmean=pop_mean).pvalue
    # print "Expected Value {} and Calculated Value {}".format(exp_p_value,p_value)
    t_test_result = p_value < exp_p_value

    return (p_value, t_test_result)
