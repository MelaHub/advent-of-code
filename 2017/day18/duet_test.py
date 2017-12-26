import unittest
from ddt import ddt, data, unpack

from duet import *

@ddt
class DuetTest(unittest.TestCase):

  def _dict_to_sorted_tuples(self, dictionary):
    return sorted([(r, v) for r, v in dictionary.iteritems()])

  @data(
    ({'a': 4}, 'snd a', {'a': 4}, 4, None, 0),
    ({'a': 4}, 'set b 42', {'a': 4, 'b': 42}, None, None, 0),
    ({'a': 4}, 'set b a', {'a': 4, 'b': 4}, None, None, 0),
    ({'a': 4}, 'add a 2', {'a': 6}, None, None, 0),
    ({'a': 4, 'b': 2}, 'add a b', {'a': 6, 'b': 2}, None, None, 0),
    ({'a': 4}, 'mod a 3', {'a': 1}, None, None, 0),
    ({'a': 6, 'b': 4}, 'mod a b', {'a': 2, 'b': 4}, None, None, 0),
    ({'a': 4}, 'rcv a', {'a': 4}, None, 4, 0),
    ({'a': 0}, 'rcv a', {'a': 0}, None, None, 0),
    ({'a': 4}, 'jgz a -2', {'a': 4}, None, None, -3),
    ({'a': 0}, 'jgz a -2', {'a': 0}, None, None, 0),
    ({'a': 4, 'b': 2}, 'jgz a b', {'a': 4, 'b': 2}, None, None, 1),
    ({'a': 0, 'b': 2}, 'jgz a b', {'a': 0, 'b': 2}, None, None, 0),
  )
  @unpack
  def test_execute(self, init_registers, instruction, expected_registers, expected_sound, expected_frequency, new_current_instruction):
    processor = Processor()
    processor.registers = {r: v for r, v in init_registers.iteritems()}
    recovered_frequency = processor.execute(instruction)
    self.assertEquals(self._dict_to_sorted_tuples(expected_registers),
                      self._dict_to_sorted_tuples(processor.registers))
    self.assertEquals(expected_sound, processor.last_played_sound)
    self.assertEquals(expected_frequency, recovered_frequency)
    self.assertEquals(new_current_instruction, processor.curr_instruction)
    
