WAITING_FOR_DATA = 'WAITING_FOR_DATA'
IDLE = 'IDLE'

class Processor(object):

  registers = {}
  last_played_sound = None
  curr_instruction = 0

  def _get_value(self, input_name):
    if input_name.strip('-').isdigit():
      return int(input_name)
    else:
      return self.registers.get(input_name, 0)

  def _parse_instruction(self, instruction):
    return instruction[0:3], instruction[4:]

  def execute(self, instruction):
    operator, parameters = self._parse_instruction(instruction)
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


class ProcessorSync(Processor):

  input_queue = None
  another_processor = None
  number_of_received_values = 0
  receive_register = None

  def __init__(self):
    self.input_queue = []

  def send_data_to(self, another_processor):
    self.another_processor = another_processor

  def execute(self, instruction):
    if self.receive_register is not None:
      return None
    operator, parameters = self._parse_instruction(instruction)
    frequency = super(ProcessorSync, self).execute(instruction)
    if operator == 'snd':
      self.another_processor.send_value(self.registers.get(parameters, 0))
    elif operator == 'rcv':
      value = None
      self.receive_register = parameters
      if len(self.input_queue):
        self.consume_data()
    return frequency

  def send_value(self, value):
    self.input_queue.append(value)
    if self.receive_register is not None:
        self.consume_data()

  def consume_data(self):
    value, input_queue = self.input_queue[0], self.input_queue[1:]
    self.registers[self.receive_register] = value
    self.number_of_received_values += 1
    self.receive_register = None


def play_instructions_from_file():
  instructions = []
  with open('duet') as f:
    instructions += [row.strip() for row in f.readlines()]
  processor = Processor()
  return processor.play_program(instructions)
