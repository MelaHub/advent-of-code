import unittest
from ddt import ddt, data, unpack

from dance import *

@ddt
class DefragTest(unittest.TestCase):

  @data(
    ('abcde', 's3', 'cdeab'),
    ('abcde', 'x1/3', 'adcbe'),
    ('abcde', 'pc/a', 'cbade'),
  )
  @unpack
  def test_move(self, input_string, dance_move, expected_string):
    self.assertEquals(expected_string, move(input_string, dance_move))

  def test_dance(self):
    choreography = ['s1', 'x3/4', 'pe/b']
    self.assertEquals('baedc', dance('abcde', choreography))

  def test_aoc_dance(self):
    self.assertEquals('bkgcdefiholnpmja', aoc_choreo())
