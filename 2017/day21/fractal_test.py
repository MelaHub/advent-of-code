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

  def test_enrich_rules(self):
    expected_rules = {
      '../.#': '##./#../...',
      '../#.': '##./#../...',
      '.#/..': '##./#../...', 
      '.#/..': '##./#../...', 
      '#./..': '##./#../...', 
      '../.#': '##./#../...', 
      '#./..': '##./#../...', 
      '.#/..': '##./#../...', 
      '../#.': '##./#../...', 
      '../#.': '##./#../...', 
      '../.#': '##./#../...', 
      '#./..': '##./#../...',
      '.#./..#/###': '#..#/..../..../#..#', 
      '.#./#../###': '#..#/..../..../#..#', 
      '###/..#/.#.': '#..#/..../..../#..#', 
      '.##/#.#/..#': '#..#/..../..../#..#', 
      '##./#.#/#..': '#..#/..../..../#..#',
      '..#/#.#/.##': '#..#/..../..../#..#',
      '###/#../.#.': '#..#/..../..../#..#',
      '###/..#/.#.': '#..#/..../..../#..#',
      '.#./#../###': '#..#/..../..../#..#',
      '#../#.#/##.': '#..#/..../..../#..#',
      '..#/#.#/.##': '#..#/..../..../#..#',
      '##./#.#/#..': '#..#/..../..../#..#',
    }
    enriched_rules = enrich_rules(expected_rules)
    self.assertEquals(sorted(expected_rules.keys()), sorted(enriched_rules.keys()))
    for key, value in expected_rules.iteritems():
      self.assertEquals(value, enriched_rules.get(key))

  @data(
    (STARTING_SQUARE, TEST_RULES['.#./..#/###'].split('/')),
    (['#.', '..'], TEST_RULES['../.#'].split('/')),
  )
  @unpack
  def test_parse_input(self, input_square, expected_output):
    self.assertEquals(expected_output, replace_square(input_square, enrich_rules(self.TEST_RULES)))
  
  @data(
    (['12', '34'], [['12', '34'], ['31', '42'], ['43', '21'], ['24', '13'], ['21', '43'], ['34', '12'], ['43', '21'], ['42', '31'], ['13', '24']]), 
    (['123', '456', '789'], [['123', '456', '789'], ['741', '852', '963'], ['987','654','321'], ['369','258','147'], ['321', '654', '987'], ['789', '456', '123'], ['987', '654', '321'], ['963', '852', '741'], ['147', '258', '369']]),
  )
  @unpack
  def test_rotate_flip_square(self, input_square, expected_squares):
    self.assertEquals(expected_squares, rotate_flip_square(input_square))

  @data(
    ([['12', '34'], ['56', '78'], ['90', 'AB'], ['CD', 'EF']], ['1256', '3478', '90CD', 'ABEF']),
    ([['111', '222', '333'], ['444', '555', '666'], ['777', '888', '999'], ['000', 'AAA', 'BBB']], ['111444', '222555', '333666', '777000', '888AAA', '999BBB']),
  )
  @unpack
  def test_merge(self, input_squares, expected_square):
    self.assertEquals(expected_square, merge(input_squares))


  @data(
    (STARTING_SQUARE, [STARTING_SQUARE]),
    (['..', '.#'], [['..', '.#']]),
    (['#..#', '....', '....', '#..#'], [['#.', '..'], ['.#', '..'], ['..', '#.'], ['..', '.#']]),
    (['##.##....', '##.....##', '#.#.#.#.#', '.#.#.#.#.', '.#...#...', '.........', '..##..##.', '#.....#..', '.#.##....'], [['##.', '##.', '#.#'], ['##.', '...', '.#.'], ['...', '.##', '#.#'], ['.#.', '.#.', '...'], ['#.#', '..#', '...'], ['.#.', '...', '...'], ['..#', '#..', '.#.'], ['#..', '...', '##.'], ['##.', '#..', '...']]),
  )
  @unpack
  def test_split_in_sub(self, input_square, expected_squares):
    self.assertEquals(expected_squares, split_square(input_square))

  def test_draw_fractal(self):
    self.assertEquals(['##.##.', '#..#..', '......', '##.##.', '#..#..', '......'], draw_fractal(STARTING_SQUARE, 2, self.TEST_RULES))
    self.assertEquals(12, count_pixels_on(2, self.TEST_RULES))
    self.assertEquals(208, count_pixels_on_from_file(5))
