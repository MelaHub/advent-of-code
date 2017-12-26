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
    elif operator == 'mod':
      register, value_or_register = parameters.split(' ')
      self.registers[register] = self.registers.get(register, 0) % self._get_value(value_or_register)
    elif operator == 'rcv':
      if self.registers.get(parameters, 0) > 0:
        frequency = self.registers[parameters]
    elif operator == 'jgz':
      register, value_or_register = parameters.split(' ')
      if self.registers.get(register, 0) > 0:
        self.curr_instruction += (self._get_value(value_or_register) - 1)
    return frequency
        
