# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def cond_prob(inp_df):
	number_of_houses = inp_df.shape[0]
	print number_of_houses
	oldtown_houses = inp_df[inp_df['Neighborhood'] == 'OldTown'].shape[0]
	prob_oldtown_house = oldtown_houses / number_of_houses
	prob_oldtown_house_suc3 =   (oldtown_houses / number_of_houses) \
								* ( (oldtown_houses -1) / (number_of_houses -1)) \
								* ((oldtown_houses-2) / (number_of_houses -2))
	return prob_oldtown_house_suc3
