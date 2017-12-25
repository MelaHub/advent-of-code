import unittest
from ddt import ddt, data, unpack

from defrag import *

@ddt
class DefragTest(unittest.TestCase):

  def test_knot_hash_to_binary(self):
    self.assertEquals('10100000110000100000000101110000', knot_hash_to_binary_row('a0c20170'))

  def test_input_string_to_hash(self):
    self.assertEquals('d4f76bdcbf838f8416ccfa8bc6d1f9e6', input_to_knot('flqrgnkx-0'))

  @data(
    ('flqrgnkx', 8108),
    # ('nbysizxe', 8216),
  )
  @unpack
  def test_number_of_used_squares(self, input_string, expected_used_squares):
    self.assertEquals(expected_used_squares, get_number_of_used_squares(input_string))

  @data(
    ('flqrgnkx', 1242),
    ('nbysizxe', 1139),
  )
  @unpack
  def test_number_of_regions(self, input_string, expected_number_of_regions):
    self.assertEquals(expected_number_of_regions, get_number_of_regions_rec(input_string))

  
