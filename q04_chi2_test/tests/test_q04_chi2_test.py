from unittest import TestCase
from ..build import chi_square
from inspect import getargspec
import pandas as pd
import numpy

df = pd.read_csv('data/house_pricing.csv')


class TestChi2_test(TestCase):
    
    def test_chi2_test(self):   # Input parameters tests
        args = getargspec(chi_square)
        self.assertEqual(len(args[0]), 1, "Expected arguments %d, Given %d" % (1, len(args[0])))

    def test_chi2_test_default(self):  # Input parameters default tests
        args = getargspec(chi_square)
        self.assertEqual(args[3], None, "Expected default values do not match given default values")

    def test_chi2_test_result_type(self):  # Return type tests
        pval, result = chi_square(df)
        self.assertIsInstance(pval, float, "Expected data type for `Chi-Square Testing` is float you are returning\
        %s" % (type(pval)))
        self.assertIsInstance(result, numpy.bool_, "Expected data type for `Chi-Square Testing` is bool you are returning\
        %s" % (type(result)))

    def test_chi2_test_result_values(self):  # Return value tests
        pval, result = chi_square(df)
        self.assertAlmostEqual(pval, 0.36760293775391745, 3, "Return `Chi-Square Testing` value does not \
        match expected value")
        self.assertFalse(result, "Return `Chi-Square Testing` value does not match expected value")
