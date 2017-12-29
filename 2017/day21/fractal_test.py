import time
import unittest
from ddt import ddt, data, unpack

from fractal import *

@ddt
class FractalTest(unittest.TestCase):

  TEST_RULES = {
    '../.#': '##./#../...',
    '.#./..#/###': '#..#/..../..../#..#'
  }

  @data(
    (STARTING_SQUARE, TEST_RULES['.#./..#/###'].split('/')),
    (['#.', '..'], TEST_RULES['../.#'].split('/')),
  )
  @unpack
  def test_parse_input(self, input_square, expected_output):
    self.assertEquals(expected_output, replace_square(input_square, self.TEST_RULES))

  @data(
    (['12', '34'], [['12', '34'], ['31', '42'], ['43', '21'], ['24', '13'], ['21', '43']]), 
    (['123', '456', '789'], [['123', '456', '789'], ['741', '852', '963'], ['987','654','321'], ['369','258','147'], ['321', '654', '987']]),
  )
  @unpack
  def test_rotate_flip_square(self, input_square, expected_squares):
    self.assertEquals(expected_squares, rotate_flip_square(input_square))

  @data(
    (STARTING_SQUARE, STARTING_SQUARE),
    (['..', '.#'], ['..', '.#']),
    (['#..#', '....', '....', '#..#'], [['#.', '..'], ['.#', '..'], ['..', '#.'], ['..', '.#']]),
    (['##.##....', '##.....##', '#.#.#.#.#', '.#.#.#.#.', '.#...#...', '.........', '..##..##.', '#.....#..', '.#.##....'], [['##.', '##.', '#.#'], ['##.', '...', '.#.'], ['...', '.##', '#.#'], ['.#.', '.#.', '...'], ['#.#', '..#', '...'], ['.#.', '...', '...'], ['..#', '#..', '.#.'], ['#..', '...', '##.'], ['##.', '#..', '...']]),
  )
  @unpack
  def test_split_in_sub(self, input_square, expected_squares):
    self.assertEquals(expected_squares, split_square(input_square))

  def test_draw_fractal(self):
    self.assertEquals([['##.', '#..', '...'], ['##.', '#..', '...'], ['##.', '#..', '...'], ['##.', '#..', '...']], draw_fractal(STARTING_SQUARE, 2, self.TEST_RULES))
