from unittest import TestCase
from ..build import confidence_interval
from inspect import getfullargspec
import pandas as pd

df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']


class TestConfidence_interval(TestCase):

    def test_confidence_interval(self):    # Input parameters tests
        args = getfullargspec(confidence_interval)
        self.assertEqual(len(args[0]), 1, "Expected arguments %d, Given %d" % (1, len(args[0])))

    def test_confidence_interval_result_low_type(self):  # Return type tests
        low, high = confidence_interval(sample)
        self.assertIsInstance(low, float, "Expected data type for `Confidence Interval` is float you are returning\
        %s" % (type(low)))

    def test_confidence_interval_result_high_type(self):
        low, high = confidence_interval(sample)
        self.assertIsInstance(high, float, "Expected data type for `Confidence Interval` is float you are returning\
        %s" % (type(high)))

    def test_confidence_interval_result_low_values(self):  # Return value tests
        low, high = confidence_interval(sample)
        self.assertAlmostEquals(low, 1492.8429310773924, 3, "Return `Confidence Interval` value does not \
        match expected value")

    def test_confidence_interval_result_hugh_values(self):
        low, high = confidence_interval(sample)
        self.assertAlmostEquals(high, 1538.0844661828817, 3, "Return `Confidence Interval` value does not \
        match expected value")

