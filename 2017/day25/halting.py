from collections import namedtuple
import re

LEFT = 'LEFT'
RIGHT = 'RIGHT'

NextStep = namedtuple('NextStep', ['value_to_be_written', 'direction', 'next_status'])

def parse_instructions_from_file(file_name):
  init_status = None
  number_of_steps = None
  instructions = None
  with open(file_name) as f:
    init_status = re.search('Begin in state (?P<init_status>.*)\.', f.readline()).group('init_status')
    number_of_steps = int(re.search('Perform a diagnostic checksum after (?P<n_steps>[0-9]+) steps.', f.readline()).group('n_steps'))
    instructions = {}
    new_state = None
    curr_value = None
    write_value = None
    direction = None
    next_status = None
    for line in f.readlines():
      if len(line.strip()) == 0:
        new_state = None
      new_state_search = re.search('In state (?P<state>.*):', line)
      if new_state_search:
        new_state = new_state_search.group('state')
      curr_value_search = re.search('If the current value is (?P<curr_value>.*):', line)
      if curr_value_search:
        curr_value = curr_value_search.group('curr_value')
      write_value_search = re.search('- Write the value (?P<new_value>.*).', line)
      if write_value_search:
        write_value = write_value_search.group('new_value')
      direction_search = re.search('- Move one slot to the (?P<direction>.*)\.', line)
      if direction_search:
        direction = direction_search.group('direction').upper()
      next_status_search = re.search('- Continue with state (?P<new_status>.*)\.', line)
      if next_status_search:
        next_status = next_status_search.group('new_status')
      if new_state is not None and curr_value is not None and write_value is not None and direction is not None and next_status is not None:
        instructions.setdefault(new_state, {})
        instructions[new_state][curr_value] = NextStep(write_value, direction, next_status)
        curr_value = None
        write_value = None
        direction = None
        next_status = None
    return init_status, number_of_steps, instructions
   

def execute_instructions(init_status, number_of_steps, instructions):
  tape = ['0']
  current_status = init_status
  current_tape_index = 0
  for i in range(number_of_steps):
    current_instructions = instructions[current_status]
    
