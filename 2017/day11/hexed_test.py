import unittest
from ddt import ddt, data, unpack

from hexed import *

@ddt
class HexEdTest(unittest.TestCase):

  @data(
    (HexTile(0, 0), 'n', HexTile(0, 2)),
    (HexTile(0, 0), 'ne', HexTile(1, 1)),
    (HexTile(0, 0), 'se', HexTile(1, -1)),
    (HexTile(0, 0), 's', HexTile(0, -2)),
    (HexTile(0, 0), 'sw', HexTile(-1, -1)),
    (HexTile(0, 0), 'nw', HexTile(-1, 1)),
  )
  @unpack
  def test_move(self, input_coordinate, direction, expected_coordinate):
    self.assertEqual(expected_coordinate, input_coordinate.move(direction))

