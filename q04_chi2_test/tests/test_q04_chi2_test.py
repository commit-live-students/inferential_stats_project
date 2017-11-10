from unittest import TestCase
from ..build import chi_square
from inspect import getfullargspec
import pandas as pd
import numpy

df = pd.read_csv('data/house_pricing.csv')


class TestChi2_test(TestCase):
    def test_chi2_test(self):

        # Input parameters tests
        args = getfullargspec(chi_square).args
        args_default = getfullargspec(chi_square).defaults
        self.assertEqual(len(args), 1, "Expected arguments %d, Given %d" % (1, len(args)))
        self.assertEqual(args_default, None, "Expected default values do not match given default values")

        # Return type tests
        pval, result = chi_square(df)
        self.assertIsInstance(pval, float, "Expected data type for `Chi-Square Testing` is float you are returning\
        %s" % (type(pval)))
        self.assertIsInstance(result, numpy.bool_, "Expected data type for `Chi-Square Testing` is bool you are returning\
        %s" % (type(result)))

        # Return value tests
        self.assertAlmostEqual(pval, 0.36760293775391745, 3, "Return `Chi-Square Testing` value does not \
        match expected value")
        self.assertFalse(result, "Return `Chi-Square Testing` value does not match expected value")
