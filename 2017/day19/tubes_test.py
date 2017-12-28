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
    self.assertEquals(((0, 4), DOWN), find_starting_point(self.TEST_GRID))

  @data(
    (Movement(Coordinate(0, 4), DOWN), Movement(Coordinate(1, 4), DOWN)),
    (Movement(Coordinate(5, 4), DOWN), Movement(Coordinate(5, 5), RIGHT)),
    (Movement(Coordinate(5, 7), DOWN), Movement(Coordinate(5, 6), LEFT)),
    (Movement(Coordinate(5, 5), RIGHT), Movement(Coordinate(5, 6), RIGHT)),
    (Movement(Coordinate(5, 7), RIGHT), Movement(Coordinate(4, 7), UP)),
    (Movement(Coordinate(1, 10), RIGHT), Movement(Coordinate(2, 10), DOWN)),
    (Movement(Coordinate(4, 7), UP), Movement(Coordinate(3, 7), UP)),
    (Movement(Coordinate(3, 13), UP), Movement(Coordinate(3, 12), LEFT)),
    (Movement(Coordinate(1, 7), UP), Movement(Coordinate(1, 8), RIGHT)),
    (Movement(Coordinate(5, 6), LEFT), Movement(Coordinate(5, 5), LEFT)),
    (Movement(Coordinate(5, 4), LEFT), Movement(Coordinate(4, 4), UP)),
    (Movement(Coordinate(1, 7), LEFT), Movement(Coordinate(2, 7), DOWN)),
  )
  @unpack
  def test_move_in_space(self, current_coordinates, next_coordinate):
    self.assertEquals(next_coordinate, move(current_coordinates, self.TEST_GRID))

    

