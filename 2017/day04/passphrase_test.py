import unittest
from ddt import ddt, data, unpack

from passphrase import *

@ddt
class PassphraseTest(unittest.TestCase):

  @data(
    ('aa bb cc dd ee', True),
    ('aa bb cc dd aa', False),
    ('aa bb cc dd aaa', True)
  )
  @unpack
  def test_is_valid_identity(self, input_pass, expected_out):
    self.assertEqual(expected_out, is_valid_identity(input_pass))

  def test_count_valid(self):
    self.assertEqual(2, count_valid_passphrases(['aa bb cc dd ee', 'aa bb cc dd aa', 'aa bb cc dd aaa'], is_valid_identity))

  def test_default_file_identity(self):
    self.assertEqual(477, count_valid_from_default_file(is_valid_identity))

  def test_default_file_anagrem(self):
    self.assertEqual(167, count_valid_from_default_file(is_valid_anagram))

  @data(
    ('abcde fghij', True),
    ('abcde xyz ecdab', False),
    ('a ab abc abd abf abj', True),
    ('iiii oiii ooii oooi oooo', True),
    ('oiii ioii iioi iiio', False)
  )
  @unpack
  def test_is_valid_anagram(self, input_pass, expected_out):
    self.assertEqual(expected_out, is_valid_anagram(input_pass))


