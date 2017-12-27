import unittest
from ddt import ddt, data, unpack

from tubes import *

@ddt
class TubesTest(unittest.TestCase):

  def test_find_starting_point(self):
    self.assertEquals((0, 3), find_starting_point(['   |     ',]))

