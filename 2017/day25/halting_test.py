import time
import unittest
from ddt import ddt, data, unpack

from halting import *

@ddt
class MoatTest(unittest.TestCase):

  def test_parse_instructions(self):
    init_status, n_steps, instructions = parse_instructions_from_file('halting_test')
    self.assertEquals('A', init_status)
    self.assertEquals(6, n_steps)
    self.assertEquals(['A', 'B'], sorted(instructions.keys()))
    self.assertEquals(
      NextStep(value_to_be_written='1', direction='RIGHT', next_status='B'),
      instructions['A']['0'])
    self.assertEquals(
      NextStep(value_to_be_written='0', direction='LEFT', next_status='B'), 
      instructions['A']['1'])
    self.assertEquals(
      NextStep(value_to_be_written='1', direction='LEFT', next_status='A'),
      instructions['B']['0'])
    self.assertEquals(
      NextStep(value_to_be_written='1', direction='RIGHT', next_status='A'),
      instructions['B']['1'])
