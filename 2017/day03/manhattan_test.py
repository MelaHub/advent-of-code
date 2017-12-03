import unittest
from ddt import ddt, data, unpack

from manhattan import *

@ddt
class ManhattanTest(unittest.TestCase):

  @data(
    (1, (0, 0)),
    (12, (2, 1)),
    (23, (0, -2)),
    (1024, (15, 16)),
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

