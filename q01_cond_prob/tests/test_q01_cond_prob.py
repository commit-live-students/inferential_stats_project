import pandas as pd
from unittest import TestCase
from ..build import cond_prob
from inspect import getfullargspec

df = pd.read_csv('data/house_pricing.csv')


class TestCond_prob(TestCase):
    def test_cond_prob(self):

        # Input parameters tests
        args = getfullargspec(cond_prob).args
        args_default = getfullargspec(cond_prob).defaults
        self.assertEqual(len(args), 1, "Expected arguments %d, Given %d" % (1, len(args)))
        self.assertEqual(args_default, None, "Expected default values do not match given default values")

        # Return type tests
        prob = cond_prob(df)
        self.assertIsInstance(prob, float, "Expected data type for `conditional Probability` is float you are returning\
                 %s" % (type(prob)))

        # Return value tests
        self.assertAlmostEqual(prob, 0.00045232831351218984, 3, "Return `Conditional Probability` value does not \
        match expected value")
