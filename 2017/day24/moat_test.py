import time
import unittest
from ddt import ddt, data, unpack

from moat import *

@ddt
class MoatTest(unittest.TestCase):

  TEST_COMPONENTS = [
    '0/2',
    '2/2',
    '2/3',
    '3/4',
    '3/5',
    '0/1',
    '10/1',
    '9/10',
  ]

  def test_instantiate_component(self):
    link = Link('3/7')
    self.assertEquals(10, link.strength)
    self.assertEquals([3, 7], link.link_types)
   
