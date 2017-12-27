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
    self.assertEquals((expected_frequency, True), recovered_frequency)
    self.assertEquals(new_current_instruction, processor.curr_instruction)

  def test_execute_sync(self):
    processor1 = ProcessorSync(1)
    processor2 = ProcessorSync(2)
    processor1.send_data_to(processor2)
    processor1.execute('set a 42')
    processor1.execute('snd a')
    self.assertEquals([42], processor2.input_queue)
    processor1.execute('rcv b')
    self.assertEquals('b', processor1.receive_register)
    processor1.execute('add b 1')
    processor1.send_value(42)
    processor1.execute('rcv b')
    self.assertEquals(None, processor1.receive_register)
    self.assertEquals(42, processor1.registers.get('b', 0))
    processor1.execute('add b 1')
    self.assertEquals(43, processor1.registers.get('b', 0))
    processor1.send_value(7)
    processor1.send_value(8)
    processor1.execute('rcv q')
    self.assertEquals(None, processor1.receive_register)
    self.assertEquals(7, processor1.registers.get('q', 0))
    self.assertEquals([8], processor1.input_queue)


  TEST_CASE1 = [
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

  TEST_CASE2 = [
    'snd 1',
    'snd 2',
    'snd p',
    'rcv a',
    'rcv b',
    'rcv c',
    'rcv d',
  ]
   
  def test_program(self):
    processor = Processor()
    self.assertEquals(4, processor.play_program(self.TEST_CASE1)) 

  def test_input(self):
    self.assertEquals(1187, play_instructions_from_file())

  def test_play_duet(self):
    self.assertEquals(1, play_duet(self.TEST_CASE1))
    self.assertEquals(3, play_duet(self.TEST_CASE2))

  def test_play_duet_from_file(self):
    self.assertEquals(5969, play_duet_from_file())
