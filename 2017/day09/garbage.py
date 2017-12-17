def get_score_for_group(input_groups):
  curr_score = 0
  number_of_nested_groups = 0
  inside_garbage = False
  i = 0
  while i < len(input_groups):
    if input_groups[i] == '!':
      i += 2
      continue
    if input_groups[i] == '<':
      inside_garbage = True
    elif input_groups[i] == '>':
      inside_garbage = False
    elif input_groups[i] == '{' and not inside_garbage:
      number_of_nested_groups += 1
    elif input_groups[i] == '}' and not inside_garbage:
      curr_score += number_of_nested_groups
      number_of_nested_groups -= 1
    i += 1
  return curr_score

def get_score_from_file():
  groups = ''
  with open('garbage') as f:
    groups += ''.join([row for row in f.readlines()])
  return get_score_for_group(groups)
