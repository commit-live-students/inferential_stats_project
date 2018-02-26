# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd
import math
df = pd.read_csv('data/house_pricing.csv')

def cond_prob(df):
    total = df[['Id','Neighborhood']].groupby('Neighborhood').count()
    total_houses = total.sum()
    Old_Town_houses = total.loc['OldTown'][0]
    Numerator = Old_Town_houses*(Old_Town_houses-1)*(Old_Town_houses-2)
    Denominator = total_houses*(total_houses-1)*(total_houses-2)
    #prob = (math.factorial(Old_Town_houses)/(math.factorial(3)*math.factorial(Old_Town_houses-3))/total_houses
    return float(Numerator/Denominator)



# Enter Code Here
