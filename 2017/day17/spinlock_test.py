import unittest
from ddt import ddt, data, unpack

from spinlock import *

@ddt
class DefragTest(unittest.TestCase):

  @data(
    (3, 1, [0, 1]),
    (3, 2, [0, 2, 1]),
    (3, 3, [0, 2, 3,1]),
    (3, 4, [0, 2, 4, 3, 1]),
    (3, 5, [0, 5, 2, 4, 3]),
    (3, 6, [2, 4, 3, 6, 1]),
    (3, 7, [0, 5, 7, 2, 4, 3]),
    (3, 8, [2, 4, 3, 8, 6, 1]),
    (3, 9, [0, 9, 5, 7, 2]),
    (3, 2017, [1512, 1134, 151, 2017, 638, 1513, 851]),
    (337, 2017, [96, 155, 1076, 2017, 600, 1368, 1332]),
  )
  @unpack
  def test_evolve(self, steps, n_times, expected_buffer):
    final_buffer = spin(n_times, steps)
    position_last_value = final_buffer.index(n_times)
    start_index = position_last_value - 3
    if start_index < 0:
      start_index = 0
    final_index = position_last_value + 4
    if final_index > len(final_buffer):
      final_index = len(final_buffer)
    test_buffer = final_buffer[start_index:final_index]
    self.assertEqual(expected_buffer, test_buffer)

  def test_value_after_zero(self):
    self.assertEquals(31220910, check_position_at(50000000, 337, 1))
