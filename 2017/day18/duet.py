WAITING_FOR_DATA = 'WAITING_FOR_DATA'
IDLE = 'IDLE'

class Processor(object):

  registers = None
  last_played_sound = None
  curr_instruction = None

  def __init__(self):
    self.registers = {}
    self.curr_instruction = 0

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
      if self._get_value(register) > 0:
        self.curr_instruction += (self._get_value(value_or_register) - 1)
    return frequency, True

  def stop_condition(self):
    return True
      
  def play_program(self, instructions):
    frequency = None
    while self.stop_condition():
      if self.curr_instruction < 0 or self.curr_instruction >= len(instructions):
        break
      instruction = instructions[self.curr_instruction]
      frequency, increment_instruction = self.execute(instruction)
      if increment_instruction:
        self.curr_instruction += 1
      if frequency is not None:
        break
    return frequency


class ProcessorSync(Processor):

  input_queue = None
  another_processor = None
  number_of_sent_values = 0
  receive_register = None
  processor_id = None

  def __init__(self, processor_id):
    super(ProcessorSync, self).__init__()
    self.input_queue = []
    self.processor_id = processor_id
    self.registers['p'] = processor_id

  def send_data_to(self, another_processor):
    self.another_processor = another_processor

  def execute(self, instruction):
    _, increment_instruction = super(ProcessorSync, self).execute(instruction)
    operator, parameters = self._parse_instruction(instruction)
    if operator == 'snd':
      self.number_of_sent_values += 1
      self.another_processor.send_value(self.registers.get(parameters, 0))
    elif operator == 'rcv':
      value = None
      self.receive_register = parameters
      if len(self.input_queue):
        self.consume_data()
      else:
        increment_instruction = False
    return None, increment_instruction

  def send_value(self, value):
    self.input_queue.append(value)

  def consume_data(self):
    value, self.input_queue = self.input_queue[0], self.input_queue[1:]
    self.registers[self.receive_register] = value
    self.receive_register = None

  def stop_condition(self):
    return self.receive_register is None or self.receive_register is not None and len(self.input_queue) > 0


def get_instructions_from_file():
  instructions = []
  with open('duet') as f:
    instructions += [row.strip() for row in f.readlines()]
  return instructions

def play_instructions_from_file():
  instructions = get_instructions_from_file()
  processor = Processor()
  return processor.play_program(instructions)

def play_duet(instructions):
  processor0 = ProcessorSync(0)
  processor1 = ProcessorSync(1)
  processor0.send_data_to(processor1)
  processor1.send_data_to(processor0)
  while True:
    processor0.play_program(instructions)
    processor1.play_program(instructions)
    if (processor0.receive_register is not None and
        processor1.receive_register is not None and
        len(processor0.input_queue) == 0 and len(processor1.input_queue) == 0):
      break
  return processor1.number_of_sent_values

def play_duet_from_file():
  return play_duet(get_instructions_from_file())

