import unittest
from ddt import ddt, data, unpack

from plumber import *

@ddt
class PlumberTest(unittest.TestCase):

  SAMPLE_INPUT = [
    '0 <-> 2',
    '1 <-> 1',
    '2 <-> 0, 3, 4',
    '3 <-> 2, 4',
    '4 <-> 2, 3, 6',
    '5 <-> 6',
    '6 <-> 4, 5'
  ]

  @data(
    ('0 <-> 2', (0, [2])),
    ('4 <-> 2, 3, 6', (4, [2, 3, 6])),
  )
  @unpack
  def test_parse_input(self, input_connection, expected_output):
    pipes = Pipes()
    expected_source, expected_links = expected_output
    source, links = pipes._parse_input(input_connection)
    self.assertEquals(expected_source, source)
    self.assertEquals(expected_links, links)

  def _init_sample_pipes(self):
    pipes = Pipes()
    for link in self.SAMPLE_INPUT:
      pipes.add_link(link)
    return pipes

  def test_add_to_graph(self):
    pipes = self._init_sample_pipes()
    self.assertEquals(7, len(pipes.graph.keys()))
    self.assertEquals([2, 3, 6], pipes.graph.get(4))

  def test_search_connected(self):
    pipes = self._init_sample_pipes()
    self.assertEquals(set([0, 2, 3, 4, 5, 6]), pipes.search_connected(0))
