import time
import unittest
from ddt import ddt, data, unpack

from virus import *

@ddt
class VirusTest(unittest.TestCase):

  TEST_MAP = [
    '..#',
    '#..',
    '...',
  ]
 
  @data(
    (INFECTED_CELL, Coordinates(0, 0, UP), Coordinates(1, 0, RIGHT), CLEAN_CELL),
    (INFECTED_CELL, Coordinates(1, 0, RIGHT), Coordinates(1, -1, DOWN), CLEAN_CELL),
    (INFECTED_CELL, Coordinates(1, -1, DOWN), Coordinates(0, -1, LEFT), CLEAN_CELL),
    (INFECTED_CELL, Coordinates(0, -1, LEFT), Coordinates(0, 0, UP), CLEAN_CELL),
    (CLEAN_CELL, Coordinates(0, 0, UP), Coordinates(-1, 0, LEFT), INFECTED_CELL),
    (CLEAN_CELL, Coordinates(-1, 0, LEFT), Coordinates(-1, -1, DOWN), INFECTED_CELL),
    (CLEAN_CELL, Coordinates(-1, -1, DOWN), Coordinates(0, -1, RIGHT), INFECTED_CELL),
    (CLEAN_CELL, Coordinates(0, -1, RIGHT), Coordinates(0, 0, UP), INFECTED_CELL),
  ) 
  @unpack
  def test_move_and_infect(self, input_cell_status, virus_starting_point, expected_position, expected_cell_status):
    virus = Virus(virus_starting_point)
    output_cell_status = virus.move_and_infect(input_cell_status)
    self.assertEquals(expected_position, virus.current_position)
    self.assertEquals(expected_cell_status, output_cell_status)
    
