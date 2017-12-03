import unittest
from ddt import ddt, data, unpack

from manhattan import *

@ddt
class ManhattanTest(unittest.TestCase):

  @data(
    (1, (0, 0)),
    (5, (-1, 1)),
    (12, (2, 1)),
    (16, (-1, 2)),
    (21, (-2, -2)),
    (23, (0, -2)),
    (1024, (-15, 16)),
  )
  @unpack
  def test_get_memory_position(self, memory_location, expected_coordinates):
    self.assertEqual(expected_coordinates, get_memory_position(memory_location))

  @data(
    (1, 0),
    (12, 3),
    (23, 2),
    (1024, 31),
    (289326, 419)
  )
  @unpack
  def test_get_manhattan_memory(self, memory_location, expected_distance):
    self.assertEqual(expected_distance, manhattan_memory(memory_location))

  @data(
    (1, 2),
    (5, 10),
    (748, 806),
    (289326, 0),
  )
  @unpack
  def test_get_sum_adiacent(self, memory_location, expected_value):
    self.assertEqual(expected_value, sum_adiacent(memory_location))

