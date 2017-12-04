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
  def test_captcha(self, input_pass, expected_out):
    self.assertEqual(expected_out, is_valid(input_pass))

  def test_count_valid(self):
    self.assertEqual(2, count_valid_passphrases(['aa bb cc dd ee', 'aa bb cc dd aa', 'aa bb cc dd aaa']))

  def test_default_file(self):
    self.assertEqual(0, count_valid_from_default_file())

