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
 
  # @data(
  #   (INFECTED_CELL, Coordinates(0, 0, UP), Coordinates(1, 0, RIGHT), CLEAN_CELL),
  #   (INFECTED_CELL, Coordinates(1, 0, RIGHT), Coordinates(1, 1, DOWN), CLEAN_CELL),
  #   (INFECTED_CELL, Coordinates(1, 1, DOWN), Coordinates(0, 1, LEFT), CLEAN_CELL),
  #   (INFECTED_CELL, Coordinates(0, 1, LEFT), Coordinates(0, 0, UP), CLEAN_CELL),
  #   (CLEAN_CELL, Coordinates(0, 0, UP), Coordinates(-1, 0, LEFT), INFECTED_CELL),
  #   (CLEAN_CELL, Coordinates(-1, 0, LEFT), Coordinates(-1, 1, DOWN), INFECTED_CELL),
  #   (CLEAN_CELL, Coordinates(-1, -1, DOWN), Coordinates(0, -1, RIGHT), INFECTED_CELL),
  #   (CLEAN_CELL, Coordinates(0, -1, RIGHT), Coordinates(0, -2, UP), INFECTED_CELL),
  # ) 
  # @unpack
  # def test_move_and_infect(self, input_cell_status, virus_starting_point, expected_position, expected_cell_status):
  #   virus = Virus(virus_starting_point)
  #   output_cell_status = virus.move_and_infect(input_cell_status)
  #   self.assertEquals(expected_position, virus.current_position)
  #   self.assertEquals(expected_cell_status, output_cell_status)
  #  
  # @data(
  #   (CLEAN_CELL, Coordinates(0, 0, UP), Coordinates(-1, 0, LEFT), WEAKENED_CELL),
  #   (CLEAN_CELL, Coordinates(-1, 0, LEFT), Coordinates(-1, 1, DOWN), WEAKENED_CELL),
  #   (CLEAN_CELL, Coordinates(-1, -1, DOWN), Coordinates(0, -1, RIGHT), WEAKENED_CELL),
  #   (CLEAN_CELL, Coordinates(0, -1, RIGHT), Coordinates(0, -2, UP), WEAKENED_CELL),
  #   (WEAKENED_CELL, Coordinates(0, 0, UP), Coordinates(0, -1, UP), INFECTED_CELL),
  #   (WEAKENED_CELL, Coordinates(-1, 0, LEFT), Coordinates(-2, 0, LEFT), INFECTED_CELL),
  #   (WEAKENED_CELL, Coordinates(-1, -1, DOWN), Coordinates(-1, 0, DOWN), INFECTED_CELL),
  #   (WEAKENED_CELL, Coordinates(0, -1, RIGHT), Coordinates(1, -1, RIGHT), INFECTED_CELL),
  #   (INFECTED_CELL, Coordinates(0, 0, UP), Coordinates(1, 0, RIGHT), FLAGGED_CELL),
  #   (INFECTED_CELL, Coordinates(1, 0, RIGHT), Coordinates(1, 1, DOWN), FLAGGED_CELL),
  #   (INFECTED_CELL, Coordinates(1, 1, DOWN), Coordinates(0, 1, LEFT), FLAGGED_CELL),
  #   (INFECTED_CELL, Coordinates(0, 1, LEFT), Coordinates(0, 0, UP), FLAGGED_CELL),
  #   (FLAGGED_CELL, Coordinates(0, 0, UP), Coordinates(0, 1, DOWN), CLEAN_CELL),
  #   (FLAGGED_CELL, Coordinates(1, 0, RIGHT), Coordinates(0, 0, LEFT), CLEAN_CELL),
  #   (FLAGGED_CELL, Coordinates(1, 1, DOWN), Coordinates(1, 0, UP), CLEAN_CELL),
  #   (FLAGGED_CELL, Coordinates(0, 1, LEFT), Coordinates(1, 1, RIGHT), CLEAN_CELL),
  # ) 
  # @unpack
  # def test_move_and_infect_enhanced(self, input_cell_status, virus_starting_point, expected_position, expected_cell_status):
  #   virus = SuperVirus(virus_starting_point)
  #   output_cell_status = virus.move_and_infect(input_cell_status)
  #   self.assertEquals(expected_position, virus.current_position)
  #   self.assertEquals(expected_cell_status, output_cell_status)

  # def test_init_grid(self):
  #   grid = init_grid(self.TEST_MAP, Virus)
  #   self.assertEquals(set([(2, 0), (0, 1)]), grid.infected_cells)
  #   self.assertEquals(Coordinates(1, 1, UP), grid.virus.current_position)

  def select_only_infected(self, grid):
    return set([key for key, value in grid.infected_cells.iteritems() if value == INFECTED_CELL])

  # def test_move_virus(self):
  #   grid = init_grid(self.TEST_MAP, Virus)
  #   self.assertEquals(set([(2, 0), (0, 1)]), self.select_only_infected(grid))
  #   grid.move_virus(1)
  #   self.assertEquals(set([(2, 0), (0, 1), (1, 1)]), self.select_only_infected(grid))
  #   grid.move_virus(1)
  #   self.assertEquals(set([(2, 0), (1, 1)]), self.select_only_infected(grid))
  #   grid.move_virus(5)
  #   self.assertEquals(set([(-1, 0), (-1.0, 1.0), (0, 1), (2, 0), (1.0, 1.0)]), self.select_only_infected(grid))
  #   self.assertEquals(5, grid.number_of_caused_infections)
  #   grid.move_virus(70-7)
  #   self.assertEquals(41, grid.number_of_caused_infections)
  #   grid.move_virus(10000 - 70)
  #   self.assertEquals(5587, grid.number_of_caused_infections)

  # def test_move_virus_from_file(self):
  #   input_grid = get_grid_from_file()
  #   grid = init_grid(input_grid, Virus)
  #   grid.move_virus(10000)
  #   self.assertEquals(5176, grid.number_of_caused_infections)

  def test_move_super_virus(self):
    grid = init_grid(self.TEST_MAP, SuperVirus)
    self.assertEquals(set([(2, 0), (0, 1)]), grid.infected_cells)
    grid.move_virus(1)
    # self.assertEquals(26, grid.number_of_caused_infections)

  # def test_move_super_virus_from_file(self):
  #   input_grid = get_grid_from_file()
  #   grid = init_grid(input_grid, Virus)
  #   grid.move_virus(10000)
  #   self.assertEquals(5176, grid.number_of_caused_infections)
