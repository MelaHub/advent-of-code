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
    link = Link(0, '3/7')
    self.assertEquals(10, link.strength)
    self.assertEquals([3, 7], link.link_types)

  def link_bridges_to_string_bridges(self, bridges):
    return [
      [str(link) for link in bridge]
        for bridge in bridges
    ]

  def test_build_possible_bridges(self):
    expected_bridges = [
      ['0/1'],
      ['0/1', '10/1'],
      ['0/1', '10/1', '9/10'],
      ['0/2'],
      ['0/2', '2/3'],
      ['0/2', '2/3', '3/4'],
      ['0/2', '2/3', '3/5'],
      ['0/2', '2/2'],
      ['0/2', '2/2', '2/3'],
      ['0/2', '2/2', '2/3', '3/4'],
      ['0/2', '2/2', '2/3', '3/5'],
    ]
    output_bridges = build_bridges(links_from_string(self.TEST_COMPONENTS))
    string_bridges = self.link_bridges_to_string_bridges(output_bridges)
    self.assertEquals(sorted([''.join(bridge) for bridge in expected_bridges]), sorted([''.join(bridge) for bridge in string_bridges]))

  def test_max_strength(self):
    self.assertEquals(31, max_strength(build_bridges(links_from_string(self.TEST_COMPONENTS))))
    self.assertEquals(1906, max_strength(build_bridges(links_from_string(links_from_file()))))

  def test_strength_longest(self):
    bridges = build_bridges(links_from_string(self.TEST_COMPONENTS))
    longest_bridges_list = longest_bridges(bridges)
    self.assertEquals(19, max_strength(longest_bridges_list))
