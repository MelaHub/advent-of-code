import unittest
from ddt import ddt, data, unpack

from coproc import *

@ddt
class CoProcessorTest(unittest.TestCase):

  def _dict_to_sorted_tuples(self, dictionary):
    return sorted([(r, v) for r, v in dictionary.iteritems()])

  @data(
    ({'a': 4}, 'sub a 3', {'a': 1}, 0),
    ({'a': 4, 'b': 1}, 'sub a b', {'a': 3, 'b': 1}, 0),
    ({'a': 4}, 'jnz a -1', {'a': 4}, -2),
    ({'a': 0}, 'jnz a -2', {'a': 0}, 0),
    ({'a': -7}, 'jnz a 2', {'a': -7}, 1),
  )
  @unpack
  def test_execute(self, init_registers, instruction, expected_registers, new_current_instruction):
    processor = CoProcessor()
    processor.registers = {r: v for r, v in init_registers.iteritems()}
    processor.execute(instruction)
    self.assertEquals(self._dict_to_sorted_tuples(expected_registers),
                      self._dict_to_sorted_tuples(processor.registers))
    self.assertEquals(new_current_instruction, processor.curr_instruction)

  def test_program(self):
    processor = CoProcessor()
    processor.play_program(get_instructions_from_file())
    self.assertEquals(6724, processor.mul_number) 

  def test_no_debug_mode(self):
    self.assertEquals(903, optimized_program()) 

