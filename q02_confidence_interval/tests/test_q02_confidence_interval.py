from unittest import TestCase
from ..build import confidence_interval
from inspect import getfullargspec
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']


class TestConfidence_interval(TestCase):
    def test_confidence_interval(self):

        # Input parameters tests
        args = getfullargspec(confidence_interval).args
        args_default = getfullargspec(confidence_interval).defaults
        self.assertEqual(len(args), 1, "Expected arguments %d, Given %d" % (1, len(args)))
        self.assertEqual(args_default, None, "Expected default values do not match given default values")

        # Return type tests
        low, high = confidence_interval(sample)
        self.assertIsInstance(low, float, "Expected data type for `Confidence Interval` is float you are returning\
        %s" % (type(low)))
        self.assertIsInstance(high, float, "Expected data type for `Confidence Interval` is float you are returning\
        %s" % (type(high)))

        # Return value tests
        self.assertAlmostEqual(low, 1492.8429310773924, 2, "Return `Confidence Interval` value does not \
        match expected value")
        self.assertAlmostEqual(high, 1538.0844661828817, 2, "Return `Confidence Interval` value does not \
        match expected value")
