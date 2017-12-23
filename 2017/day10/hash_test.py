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
    reversed_list, _, _ = reverse_for_each_length([0, 1, 2, 3, 4], [3, 4, 1, 5])
    self.assertEquals([3, 4, 2, 1, 0], reversed_list)

  def test_knot_list_sample(self):
    self.assertEquals(12, knot_list([0, 1, 2, 3, 4], [3, 4, 1, 5]))

  def test_knot_list(self):
    self.assertEquals(212, knot_list(range(0, 256), [212,254,178,237,2,0,1,54,167,92,117,125,255,61,159,164]))

  @data(
    ('1,2,3', [49,44,50,44,51]),
  )
  @unpack
  def test_convert_to_ascii(self, input_lengths, expected_ascii):
    self.assertEquals(expected_ascii, convert_to_ascii(input_lengths))

  def test_get_standard_lengths(self):
    self.assertEquals([49, 44, 50, 44, 51, 17, 31, 73, 47, 23], get_standard_lengths('1,2,3'))

  def test_get_dense_hash(self):
    self.assertEquals(64, get_block_dense_hash([65,  27,  9,  1,  4,  3,  40,  50,  91,  7,  6,  0,  2,  5,  68,  22]))

  # @data(
  #   ('', 'a2582a3a0e66e6e86e3812dcb672a272'),
  #   ('AoC 2017', '33efeb34ea91902bb2f59c9920caa6cd'),
  #   ('1,2,3', '3efbe78a8d82f29979031a4aa0b16a9d'),
  #   ('1,2,4', '63960835bcdc130f0b66d7ff4f6a5a8e')
  # )
  # @unpack
  # def test_knot_hash(self, input_string, expected_hash):
  #   self.assertEquals(expected_hash, knot_hash(input_string))

