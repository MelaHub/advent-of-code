import unittest
from ddt import ddt, data, unpack

from garbage import *

@ddt
class RegisterTest(unittest.TestCase):

  @data(
    ('{}', 1),
    ('{{{}}}', 6),
    ('{{},{}}', 5),
    ('{{{},{},{{}}}}', 16),
    ('{<a>,<a>,<a>,<a>}', 1),
    ('{{<ab>},{<ab>},{<ab>},{<ab>}}', 9),
    ('{{<!!>},{<!!>},{<!!>},{<!!>}}', 9),
    ('{{<a!>},{<a!>},{<a!>},{<ab>}}', 3),
  )
  @unpack
  def test_get_score(self, input_groups, expected_score):
    self.assertEqual(expected_score, get_score_for_group(input_groups))

  def test_parse_file(self):
    self.assertEqual(0, get_score_from_file())
