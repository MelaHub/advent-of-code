import unittest
from ddt import ddt, data, unpack

from maze import *

@ddt
class PassphraseTest(unittest.TestCase):

  def _move_and_check(self, input_values, expected_out, fn):
    input_maze, current_index = input_values
    expected_maze, expected_index = expected_out
    actual_maze, actual_index = fn(input_maze, current_index)
    self.assertListEqual(expected_maze, actual_maze) and self.assertEqual(expected_index, current_index)

  @data(
    (([0, 3, 0, 1, -3], 0), ([1, 3, 0, 1, -3], 0)),
    (([1, 3, 0, 1, -3], 0), ([2, 3, 0, 1, -3], 1)),
    (([2, 3, 0, 1, -3], 1), ([2, 4, 0, 1, -3], 4)),
    (([2, 4, 0, 1, -3], 4), ([2, 4, 0, 1, -2], 1)),
    (([2, 4, 0, 1, -2], 1), ([2, 5, 0, 1, -2], 5)),
  )
  @unpack
  def test_is_valid_identity(self, input_values, expected_out):
    self._move_and_check(input_values, expected_out, move_in_maze)

  @data(
    (([0, 3, 0, 1, -3], 0), ([1, 3, 0, 1, -3], 0)),
    (([1, 3, 0, 1, -3], 0), ([2, 3, 0, 1, -3], 1)),
    (([2, 3, 0, 1, -3], 1), ([2, 2, 0, 1, -3], 4)),
    (([2, 2, 0, 1, -3], 4), ([2, 2, 0, 1, -2], 1)),
    (([2, 2, 0, 1, -2], 1), ([2, 3, 0, 1, -2], 3)),
  )
  @unpack
  def test_is_valid_identity(self, input_values, expected_out):
    self._move_and_check(input_values, expected_out, move_weird_in_maze)

  def test_solve_maze_works(self):
    self.assertEqual(5, solve_maze_non_rec([0, 3, 0, 1, -3], move_in_maze))

  def test_solve_weird_maze_works(self):
    self.assertEqual(10, solve_maze_non_rec([0, 3, 0, 1, -3], move_weird_in_maze))

  def test_solve_maze_from_file_works(self):
    self.assertEqual(372139, solve_maze_from_file(move_in_maze))

  def test_solve_weird_maze_from_file_works(self):
    self.assertEqual(29629538, solve_maze_from_file(move_weird_in_maze))
