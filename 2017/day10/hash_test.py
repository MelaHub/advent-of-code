import unittest
from ddt import ddt, data, unpack

from hash import *

@ddt
class HashTest(unittest.TestCase):

  @data(
    ([0, 1, 2, 3, 4], 0, 3, [2, 1, 0, 3, 4]),
    ([2, 1, 0, 3, 4], 3, 4, [4, 3, 0, 1, 2]),
    ([4, 3, 0, 1, 2], 1, 5, [3, 4, 2, 1, 0]),
    ([3, 4, 2, 1, 0], 1, 4, [3, 0, 1, 2, 4]),
  )
  @unpack
  def test_reverse_elements(self, input_list, current_position, reverse_length, expected_output):
    self.assertEqual(expected_output, reverse_elements(input_list, current_position, reverse_length))

  def test_sample_lengths(self):
    self.assertEquals([3, 4, 2, 1, 0], reverse_for_each_length([0, 1, 2, 3, 4], [3, 4, 1, 5]))

  def test_hash_sample(self):
    self.assertEquals(12, hash([0, 1, 2, 3, 4], [3, 4, 1, 5]))

  def test_hash(self):
    self.assertEquals(12, hash(range(0, 256), [212,254,178,237,2,0,1,54,167,92,117,125,255,61,159,164]))

