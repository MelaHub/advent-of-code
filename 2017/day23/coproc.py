from day18.duet import Processor
from math import sqrt
from itertools import count, islice


class CoProcessor(Processor):

  mul_number = None

  def __init__(self, debug_mode=True):
    super(CoProcessor, self).__init__()
    self.registers = {chr(i): 0 for i in range(ord('a'), ord('h') + 1)}
    if not debug_mode:
      self.registers['a'] = 1
    self.mul_number = 0

  def execute(self, instruction):
    operator, parameters = self._parse_instruction(instruction)
    frequency, increment_instructions = super(CoProcessor, self).execute(instruction)
    if operator == 'sub':
      register, value_or_register = parameters.split(' ')
      self.registers[register] = self.registers.get(register, 0) - self._get_value(value_or_register)
    elif operator == 'jnz':
      register, value_or_register = parameters.split(' ')
      if self._get_value(register) != 0:
        self.curr_instruction += (self._get_value(value_or_register) - 1)
    elif operator == 'mul':
      self.mul_number += 1
    return frequency, True

def get_instructions_from_file():
  instructions = []
  with open('day23/coproc') as f:
    instructions += [row.strip() for row in f.readlines()]
  return instructions

def is_prime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))


def optimized_program():

  b = 84 * 100 + 100000
  c = b + 17000
  h = 0

  for i in range(b, c + 1, 17):
    if not is_prime(i):
      h += 1

  return h
  
