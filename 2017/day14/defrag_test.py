import unittest
from ddt import ddt, data, unpack

from defrag import *

@ddt
class DefragTest(unittest.TestCase):

  def test_knot_hash_to_binary(self):
    self.assertEquals('10100000110000100000000101110000', knot_hash_to_binary_row('a0c20170'))

  def test_input_string_to_hash(self):
    self.assertEquals('', input_to_know('flqrgnkx-0'))
