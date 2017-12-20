import unittest
from ddt import ddt, data, unpack

from garbage import *

@ddt
class RegisterTest(unittest.TestCase):

  @data(
    ('{}', [('{}', 1)], []),
    ('{{{}}}', [('{}', 3), ('{{}}', 2), ('{{{}}}', 1)], []),
    ('{{},{}}', [('{}', 2), ('{}', 2), ('{{},{}}', 1)], []),
    ('{{{},{},{{}}}}', [('{}', 3), ('{}', 3), ('{}', 4), ('{{}}', 3), ('{{},{},{{}}}', 2), ('{{{},{},{{}}}}', 1)], []),
    ('{<a>,<a>,<a>,<a>}', [('{,,,}', 1)], ['<a>', '<a>', '<a>', '<a>']),
    ('{{<ab>},{<ab>},{<ab>},{<ab>}}', [('{}', 2), ('{}', 2), ('{}', 2), ('{}', 2), ('{{},{},{},{}}', 1)], ['<ab>', '<ab>', '<ab>', '<ab>']),
    ('{{<!!>},{<!!>},{<!!>},{<!!>}}', [('{}', 2), ('{}', 2), ('{}', 2), ('{}', 2), ('{{},{},{},{}}', 1)], ['<!!>', '<!!>', '<!!>', '<!!>']),
    ('{{<a!>},{<a!>},{<a!>},{<ab>}}', [('{}', 2), ('{{}}', 1)], ['<a!>},{<a!>},{<a!>},{<ab>']),
  )
  @unpack
  def test_find_groups(self, input_groups, expected_groups, expected_garbage):
    groups, garbage = find_groups_in_string(input_groups)
    self.assertEqual(expected_groups, groups)
    self.assertEqual(expected_garbage, garbage)

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
    self.assertEqual(12396, get_score_from_file())

  def test_num_char(self):
    self.assertEqual(0, get_num_non_cancelled_from_file())

  @data(
    ('<>', 0),
    ('<random characters>', 17),
    ('<<<<>', 3),
    ('<{!>}>', 2),
    ('<!!>', 0),
    ('<!!!>>', 0),
    ('<{o"i!a,<{i<a>', 10),
  )
  @unpack
  def test_num_char_clean_garbage(self, input_garbage, expected_count_chars):
    self.assertEqual(expected_count_chars, count_valid_chars(input_garbage))


