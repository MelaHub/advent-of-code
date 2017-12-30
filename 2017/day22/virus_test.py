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
    (INFECTED_CELL, Coordinates(1, 0, RIGHT), Coordinates(1, 1, DOWN), CLEAN_CELL),
    (INFECTED_CELL, Coordinates(1, 1, DOWN), Coordinates(0, 1, LEFT), CLEAN_CELL),
    (INFECTED_CELL, Coordinates(0, 1, LEFT), Coordinates(0, 0, UP), CLEAN_CELL),
    (CLEAN_CELL, Coordinates(0, 0, UP), Coordinates(-1, 0, LEFT), INFECTED_CELL),
    (CLEAN_CELL, Coordinates(-1, 0, LEFT), Coordinates(-1, 1, DOWN), INFECTED_CELL),
    (CLEAN_CELL, Coordinates(-1, -1, DOWN), Coordinates(0, -1, RIGHT), INFECTED_CELL),
    (CLEAN_CELL, Coordinates(0, -1, RIGHT), Coordinates(0, -2, UP), INFECTED_CELL),
  ) 
  @unpack
  def test_move_and_infect(self, input_cell_status, virus_starting_point, expected_position, expected_cell_status):
    virus = Virus(virus_starting_point)
    output_cell_status = virus.move_and_infect(input_cell_status)
    self.assertEquals(expected_position, virus.current_position)
    self.assertEquals(expected_cell_status, output_cell_status)
   
  def test_init_grid(self):
    grid = init_grid(self.TEST_MAP)
    self.assertEquals(set([(2, 0), (0, 1)]), grid.infected_cells)
    self.assertEquals(Coordinates(1, 1, UP), grid.virus.current_position)

  def test_move_virus(self):
    grid = init_grid(self.TEST_MAP)
    self.assertEquals(set([(2, 0), (0, 1)]), grid.infected_cells)
    grid.move_virus(1)
    self.assertEquals(set([(2, 0), (0, 1), (1, 1)]), grid.infected_cells)
    grid.move_virus(1)
    self.assertEquals(set([(2, 0), (1, 1)]), grid.infected_cells)
    grid.move_virus(5)
    self.assertEquals(set([(-1, 0), (-1.0, 1.0), (0, 1), (2, 0), (1.0, 1.0)]), grid.infected_cells)
    self.assertEquals(5, grid.number_of_caused_infections)
    grid.move_virus(70-7)
    self.assertEquals(41, grid.number_of_caused_infections)
    grid.move_virus(10000 - 70)
    self.assertEquals(5587, grid.number_of_caused_infections)

  def test_move_virus_from_file(self):
    input_grid = get_grid_from_file()
    grid = init_grid(input_grid)
    grid.move_virus(10000)
    self.assertEquals(5176, grid.number_of_caused_infections)
