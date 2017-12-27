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
    ({'a': 4}, 'mul a 2', {'a': 8}, None, None, 0),
    ({'a': 4, 'b': 3}, 'mul a b', {'a': 12, 'b': 3}, None, None, 0),
    ({'a': 4}, 'mod a 3', {'a': 1}, None, None, 0),
    ({'a': 6, 'b': 4}, 'mod a b', {'a': 2, 'b': 4}, None, None, 0),
    ({'a': 4}, 'rcv a', {'a': 4}, 7, 7, 0),
    ({'a': 0}, 'rcv a', {'a': 0}, None, None, 0),
    ({'a': 4}, 'jgz a -2', {'a': 4}, None, None, -3),
    ({'a': 0}, 'jgz a -2', {'a': 0}, None, None, 0),
    ({'a': 4, 'b': 2}, 'jgz a b', {'a': 4, 'b': 2}, None, None, 1),
    ({'a': 0, 'b': 2}, 'jgz a b', {'a': 0, 'b': 2}, None, None, 0),
  )
  @unpack
  def test_execute(self, init_registers, instruction, expected_registers, expected_sound, expected_frequency, new_current_instruction):
    processor = Processor()
    if expected_frequency is not None:
      processor.last_played_sound = expected_frequency
    processor.registers = {r: v for r, v in init_registers.iteritems()}
    recovered_frequency = processor.execute(instruction)
    self.assertEquals(self._dict_to_sorted_tuples(expected_registers),
                      self._dict_to_sorted_tuples(processor.registers))
    self.assertEquals(expected_sound, processor.last_played_sound)
    self.assertEquals(expected_frequency, recovered_frequency)
    self.assertEquals(new_current_instruction, processor.curr_instruction)

  def test_execute_sync(self):
    processor1 = ProcessorSync()
    processor2 = ProcessorSync()
    processor1.send_data_to(processor2)
    processor1.execute('set a 42')
    processor1.execute('snd a')
    self.assertEquals([42], processor2.input_queue)
    processor1.execute('rcv b')
    self.assertEquals('b', processor1.receive_register)
    processor1.execute('add b 1')
    self.assertEquals('b', processor1.receive_register)
    self.assertEquals(0, processor1.registers.get('b', 0))
    processor1.send_value(42)
    self.assertEquals(None, processor1.receive_register)
    self.assertEquals(42, processor1.registers.get('b', 0))
    processor1.execute('add b 1')
    self.assertEquals(None, processor1.receive_register)
    self.assertEquals(43, processor1.registers.get('b', 0))


  TEST_CASE = [
    'set a 1',
    'add a 2',
    'mul a a',
    'mod a 5',
    'snd a',
    'set a 0',
    'rcv a',
    'jgz a -1',
    'set a 1',
    'jgz a -2'
  ]
   
  def test_program(self):
    processor = Processor()
    self.assertEquals(4, processor.play_program(self.TEST_CASE)) 

  def test_input(self):
    self.assertEquals(1187, play_instructions_from_file())
