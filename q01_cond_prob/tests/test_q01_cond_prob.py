import pandas as pd
from unittest import TestCase
from ..build import cond_prob
from inspect import getargspec

df = pd.read_csv('data/house_pricing.csv')


class TestCond_prob(TestCase):

    def test_arguments(self):            # Input parameters tests
        args = getargspec(cond_prob)
        self.assertEqual(len(args[0]), 1, "Expected arguments %d, Given %d" % (1, len(args[0])))

    def test_arguments_default(self):    # Input default parameter tests
        args = getargspec(cond_prob)    
        self.assertEqual(args[3], None, "Expected default values do not match given default values")

    def test_return_result_type(self):    # Return type tests
        prob = cond_prob(df)
        self.assertIsInstance(prob, float, "Expected data type for `conditional Probability` is float you are returning\
                 %s" % (type(prob)))

    def test_return_result_value(self):    # Return value tests
        prob = cond_prob(df)
        self.assertAlmostEqual(prob, 0.00045232831351218984, 3, "Return `Conditional Probability` value does not \
        match expected value")
