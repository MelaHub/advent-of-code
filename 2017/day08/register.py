import collections
import re


class Instruction():

  register = None
  operation = None
  value = None
  condition_register = None
  condition = None
  condition_value = None

  def __init__(self, instruction):
    self.register, self.operation, value, _, self.condition_register, self.condition, condition_value = instruction.split(' ')
    self.value = int(value)
    self.condition_value = int(condition_value)

  def _is_condition_valid(self, register):
    value = register.setdefault(self.condition_register, 0)
    condition = '%s %s %s' % (value, self.condition, self.condition_value)
    return eval(condition)

  def _apply_operation(self, register):
    operator = None
    if self.operation == 'inc':
      operator = '+'
    elif self.operation == 'dec':
      operator = '-'
    else:
      raise Exception('Operation not supported')
    new_value = '%d %s %d' % (
      register.setdefault(self.register, 0), operator, self.value)
    register[self.register] = eval(new_value)

  def apply(self, register):
    if self._is_condition_valid(register):
      self._apply_operation(register)


def apply_to_register(register, list_of_instructions):
  for instruction in list_of_instructions:
    i = Instruction(instruction)
    i.apply(register)

def max_value_in_register(register):
  return max(register.values())

def max_value_in_instructions_from_file():
  instructions = []
  with open('register') as f:
    instructions = [row.strip() for row in f.readlines()]
  register = {}
  apply_to_register(register, instructions)
  return max_value_in_register(register)
  
