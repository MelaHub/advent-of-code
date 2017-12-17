import unittest
from ddt import ddt, data, unpack

from register import *

@ddt
class RegisterTest(unittest.TestCase):

  @data(
    ('b inc 5 if a > 1', ('b', 'inc', 5, 'a', '>', 1)),
    ('c dec -10 if a >= 1', ('c', 'dec', -10, 'a', '>=', 1))
  )
  @unpack
  def test_parse_input(self, input_instruction, expected_instruction):
    instruction = Instruction(input_instruction)
    register, operation, value, condition_register, condition, condition_value = expected_instruction
    self.assertEqual(register, instruction.register)
    self.assertEqual(operation, instruction.operation)
    self.assertEqual(value, instruction.value)
    self.assertEqual(condition_register, instruction.condition_register)
    self.assertEqual(condition, instruction.condition)
    self.assertEqual(condition_value, instruction.condition_value)

  @data(
    ('b inc 5 if a > 1', False),
    ('c dec -10 if a >= 1', True),
    ('c dec -10 if a < 1', False),
    ('c dec -10 if a <= 1', True),
    ('c dec -10 if a == 1', True),
    ('c dec -10 if a != 1', False),
  )
  @unpack
  def test_is_condition_valid(self, input_instruction, expected_output):
    instruction = Instruction(input_instruction)
    self.assertEqual(expected_output, instruction._is_condition_valid({'a': 1}))

  @data(
    ('b inc 5 if a > 1', {'a': 1, 'b': 5}),
    ('c dec -10 if a >= 1', {'a': 1, 'c': 10}),
  )
  @unpack
  def test_apply_operation(self, input_instruction, expected_dict):
    instruction = Instruction(input_instruction)
    register = {'a': 1}
    instruction._apply_operation(register)
    self.assertEqual(sorted(expected_dict.keys()), sorted(register.keys()))
    for key in expected_dict:
      self.assertEqual(expected_dict.get(key), register.get(key))
   
  def test_apply_to_empty_register(self):
    instructions = [
      'b inc 5 if a > 1',
      'a inc 1 if b < 5',
      'c dec -10 if a >= 1',
      'c inc -20 if c == 10']
    register = {}
    max_value_ever = apply_to_register(register, instructions)
    self.assertEqual(1, register['a'])
    self.assertEqual(0, register['b'])
    self.assertEqual(-10, register['c'])
    self.assertEqual(1, max_value_in_register(register))
    self.assertEqual(10, max_value_ever)

  def test_max_value_from_file(self):
    max_value, max_value_ever = max_value_in_instructions_from_file()
    self.assertEqual(5221, max_value)
    self.assertEqual(7491, max_value_ever)
