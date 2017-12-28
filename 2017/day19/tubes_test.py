import unittest
from ddt import ddt, data, unpack

from tubes import *

@ddt
class TubesTest(unittest.TestCase):

  TEST_GRID = [
   '    |          ',
   '    |  +--+    ',
   '    A  |  C    ',
   'F---|----E|--+ ',
   '    |  |  |  D ',
   '    +B-+  +--+ ',
  ]

  def test_find_starting_point(self):
    self.assertEquals(Position(Coordinate(0, 4), DOWN), find_starting_point(self.TEST_GRID))

  @data(
    (Position(Coordinate(0, 4), DOWN), Position(Coordinate(1, 4), DOWN)),
    (Position(Coordinate(5, 4), DOWN), Position(Coordinate(5, 5), RIGHT)),
    (Position(Coordinate(5, 7), DOWN), Position(Coordinate(5, 6), LEFT)),
    (Position(Coordinate(5, 5), RIGHT), Position(Coordinate(5, 6), RIGHT)),
    (Position(Coordinate(5, 7), RIGHT), Position(Coordinate(4, 7), UP)),
    (Position(Coordinate(1, 10), RIGHT), Position(Coordinate(2, 10), DOWN)),
    (Position(Coordinate(4, 7), UP), Position(Coordinate(3, 7), UP)),
    (Position(Coordinate(3, 13), UP), Position(Coordinate(3, 12), LEFT)),
    (Position(Coordinate(1, 7), UP), Position(Coordinate(1, 8), RIGHT)),
    (Position(Coordinate(5, 6), LEFT), Position(Coordinate(5, 5), LEFT)),
    (Position(Coordinate(5, 4), LEFT), Position(Coordinate(4, 4), UP)),
    (Position(Coordinate(1, 7), LEFT), Position(Coordinate(2, 7), DOWN)),
  )
  @unpack
  def test_move_in_space(self, current_coordinates, next_coordinate):
    self.assertEquals(next_coordinate, move(current_coordinates, self.TEST_GRID))

  def test_follow_tubes(self):
    self.assertEquals(('ABCDEF',38), follow_the_tubes(self.TEST_GRID))
    self.assertEquals(('GPALMJSOY', 16204), follow_the_tubes_from_file())

