def move(input_string, dance_move):
  prefix, argument = dance_move[0], dance_move[1:]
  if prefix == 's':
    return '%s%s' % (input_string[-int(argument):], input_string[0:-int(argument)])
  elif prefix =='x':
    args = [int(a) for a in argument.split('/')]
    pos_a = min(args)
    pos_b = max(args)
    return '%s%s%s%s%s' % (input_string[:pos_a], input_string[pos_b], input_string[pos_a + 1:pos_b], input_string[pos_a], input_string[pos_b + 1:])
  elif prefix == 'p':
    find_programs = argument.split('/')
    program_pos = [i for i, p in enumerate(input_string) if p in find_programs]
    return move(input_string, 'x%d/%d' % (program_pos[0], program_pos[1]))

def dance_gen(start_configuration, choreography):
  configuration = start_configuration
  for step in choreography:
    configuration = move(configuration, step)
  return configuration

def dance(start_configuration, choreography, number_of_executions):
  configuration = start_configuration
  seen_configurations = []
  looping_at = None
  for i in xrange(number_of_executions):
    configuration = dance_gen(configuration, choreography)
    if configuration in seen_configurations:
      looping_at = i
      break
    seen_configurations.append(configuration)
  if looping_at is not None:
    configuration = start_configuration
    for i in xrange(number_of_executions % looping_at):
      configuration = dance_gen(configuration, choreography)
  return configuration
    

def aoc_choreo(number_of_executions):
  choreography = []
  with open('choreography') as f:
    choreography += ''.join(f.readlines()).strip().split(',')
  start_configuration = ''.join([chr(ord('a') + i) for i in range(16)])
  return dance(start_configuration, choreography, number_of_executions)

