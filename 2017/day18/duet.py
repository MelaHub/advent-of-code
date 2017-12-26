class Processor(object):

  registers = {}
  last_played_sound = None
  curr_instruction = 0

  def _get_value(self, input_name):
    if input_name.strip('-').isdigit():
      return int(input_name)
    else:
      return self.registers.get(input_name, 0)

  def execute(self, instruction):
    operator = instruction[0:3]
    parameters = instruction[4:]
    frequency = None
    if operator == 'snd':
      self.last_played_sound = self.registers.setdefault(parameters, 0)
    elif operator =='set':
      register, value_or_register = parameters.split(' ')
      self.registers[register] = self._get_value(value_or_register)
    elif operator == 'add':
      register, value_or_register = parameters.split(' ')
      self.registers[register] = self.registers.get(register, 0) + self._get_value(value_or_register)
    elif operator == 'mul':
      register, value_or_register = parameters.split(' ')
      self.registers[register] = self.registers.get(register, 0) * self._get_value(value_or_register)
    elif operator == 'mod':
      register, value_or_register = parameters.split(' ')
      self.registers[register] = self.registers.get(register, 0) % self._get_value(value_or_register)
    elif operator == 'rcv':
      if self.registers.get(parameters, 0) > 0:
        frequency = self.last_played_sound
    elif operator == 'jgz':
      register, value_or_register = parameters.split(' ')
      if self.registers.get(register, 0) > 0:
        self.curr_instruction += (self._get_value(value_or_register) - 1)
    return frequency
      
  def play_program(self, instructions):
    self.curr_instruction = 0
    frequency = None
    while True:
      if self.curr_instruction < 0 or self.curr_instruction >= len(instructions):
        break
      instruction = instructions[self.curr_instruction]
      frequency = self.execute(instruction)
      if frequency is not None:
        break
      self.curr_instruction += 1
    return frequency


def play_instructions_from_file():
  instructions = []
  with open('duet') as f:
    instructions += [row.strip() for row in f.readlines()]
  processor = Processor()
  return processor.play_program(instructions)
