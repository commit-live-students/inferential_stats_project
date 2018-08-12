# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def cond_prob(data):
    population = len(data)
    oldTown_houses = data[data['Neighborhood'] == 'OldTown']
    event = len(oldTown_houses)

    probability = (event/population)
    probability_2 = ((event-1)/(population-1))
    probability_3 = ((event-2)/(population-2))

    overall_probability = probability* probability_2 *probability_3
    return overall_probability

# print type(cond_prob(df))
