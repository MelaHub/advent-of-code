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

