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
