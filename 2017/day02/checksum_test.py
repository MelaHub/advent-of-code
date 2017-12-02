import unittest
from ddt import ddt, data, unpack

from checksum import *

@ddt
class ChecksumTest(unittest.TestCase):

  @data(
    ([5, 1, 9, 5], 8),
    ([7, 5, 3], 4),
    ([2, 4, 6, 8], 6)
  )
  @unpack
  def test_get_min_max_checksum(self, input_code, expected_out):
    self.assertEqual(expected_out, get_min_max_checksum(input_code))

  @data(
    ([5, 9, 2, 8], 4),
    ([9, 4, 7, 3], 3),
    ([3, 8, 6, 5], 2)
  )
  @unpack
  def test_evently_divisible(self, input_code, expected_out):
    self.assertEqual(expected_out, evenly_divisible_checksum(input_code))

  @data(
    ('5 1 9 5\n7\t5 3\n2 4 6 8', 18)
  )
  @unpack
  def test_checksum(self, input_code, expected_out):
    self.assertEqual(expected_out, get_checksum(input_code, get_min_max_checksum))

  def test_split_row(self):
    self.assertEqual([5, 1, 9, 5], split_row('5\t1  9  \t5')) 

  def test_min_max_from_file(self):
    self.assertEqual(44216, checksum_from_file('input_min_max', get_min_max_checksum))

  def test_evently_divisible_from_file(self):
    self.assertEqual(320, checksum_from_file('input_divisor', evenly_divisible_checksum))
