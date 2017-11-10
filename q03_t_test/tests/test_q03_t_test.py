from unittest import TestCase
from ..build import t_statistic
from inspect import getfullargspec
import pandas as pd
import numpy

df = pd.read_csv('data/house_pricing.csv')


class TestTTest(TestCase):
    def test_t_test(self):

        # Input parameters tests
        args = getfullargspec(t_statistic).args
        args_default = getfullargspec(t_statistic).defaults
        self.assertEqual(len(args), 1, "Expected arguments %d, Given %d" % (1, len(args)))
        self.assertEqual(args_default, None, "Expected default values do not match given default values")

        # Return type tests
        pval, result = t_statistic(df)
        self.assertIsInstance(pval, float, "Expected data type for `Hypothesis Testing` is float you are returning\
                %s" % (type(pval)))
        self.assertIsInstance(result, numpy.bool_, "Expected data type for `Hypothesis Testing` is bool you are returning\
                %s" % (type(result)))

        # Return value tests
        self.assertAlmostEqual(pval, 0.51158698884870502, 3, "Return `Hypothesis Testing` value does not \
        match expected value")
        self.assertFalse(result, "Return `Hypothesis Testing` value does not match expected value")
