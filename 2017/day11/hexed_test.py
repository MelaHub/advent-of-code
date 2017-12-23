import unittest
from ddt import ddt, data, unpack

from hexed import *

@ddt
class HexEdTest(unittest.TestCase):

  @data(
    (HexTile(0, 0), N, HexTile(0, 2)),
    (HexTile(0, 0), NE, HexTile(1, 1)),
    (HexTile(0, 0), SE, HexTile(1, -1)),
    (HexTile(0, 0), S, HexTile(0, -2)),
    (HexTile(0, 0), SW, HexTile(-1, -1)),
    (HexTile(0, 0), NW, HexTile(-1, 1)),
  )
  @unpack
  def test_move(self, input_coordinate, direction, expected_coordinate):
    self.assertEqual(expected_coordinate, input_coordinate.move(direction))

  @data(
    ('ne,ne,ne', HexTile(3, 3)),
    ('ne,ne,sw,sw', HexTile(0, 0)),
    ('ne,ne,s,s', HexTile(2, -2)),
    ('se,sw,se,sw,sw', HexTile(-1, -5)),
    ('se,ne,se,ne,se', HexTile(5, -1))
  )
  @unpack
  def test_follow_path(self, path, expected_coordinate):
    self.assertEqual(expected_coordinate, follow_path(HexTile(0, 0), path))

  @data(
    (HexTile(3, 3), 3),
    (HexTile(0, 0), 0),
    (HexTile(2, -2), 2),
    (HexTile(-1, -5), 3),
    (HexTile(5, -1), 5),
  )
  @unpack
  def test_shortest_path_len(self, ending_point, expected_path):
    self.assertEqual(expected_path, find_shortest_path(HexTile(0, 0), ending_point))

