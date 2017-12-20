OPEN_GARBAGE = '<'
CLOSE_GARBAGE = '>'
OPEN_GROUP = '{'
CLOSE_GROUP = '}'
IGNORE_NEXT = '!'

def find_groups_in_string(input_groups):
  groups = []
  garbage = []
  group_stacks = []
  inside_garbage = False
  i = 0
  while i < len(input_groups):
    if input_groups[i] == IGNORE_NEXT:
      garbage[-1] += '%s%s' % (input_groups[i], input_groups[i+1])
      i += 2
      continue
    if input_groups[i] == OPEN_GARBAGE and not inside_garbage:
      inside_garbage = True
      garbage += input_groups[i]
    elif input_groups[i] == CLOSE_GARBAGE and inside_garbage:
      garbage[-1] += input_groups[i]
      inside_garbage = False
    elif input_groups[i] == OPEN_GROUP and not inside_garbage:
      group_stacks += input_groups[i]
    elif input_groups[i] == CLOSE_GROUP and not inside_garbage:
      group_stacks[-1] += input_groups[i]
      full_group = group_stacks[-1]
      groups += ((full_group, len(group_stacks)),)
      group_stacks = group_stacks[:-1]
      if len(group_stacks):
        group_stacks[-1] += full_group
    elif len(group_stacks):
      if inside_garbage:
        garbage[-1] += input_groups[i]
      else:
        group_stacks[-1] += input_groups[i]
    i += 1
  return groups, garbage

def get_score_for_group(input_groups):
  groups, garbage = find_groups_in_string(input_groups)
  return sum([score for _, score in groups])

def get_score_for_group2(input_groups):
  curr_score = 0
  number_of_nested_groups = 0
  inside_garbage = False
  i = 0
  while i < len(input_groups):
    if input_groups[i] == IGNORE_NEXT:
      i += 2
      continue
    if input_groups[i] == OPEN_GARBAGE:
      inside_garbage = True
    elif input_groups[i] == CLOSE_GARBAGE:
      inside_garbage = False
    elif input_groups[i] == OPEN_GROUP and not inside_garbage:
      number_of_nested_groups += 1
    elif input_groups[i] == CLOSE_GROUP and not inside_garbage:
      curr_score += number_of_nested_groups
      number_of_nested_groups -= 1
    i += 1
  return curr_score

def get_score_from_file():
  groups = ''
  with open('garbage') as f:
    groups += ''.join([row for row in f.readlines()])
  return get_score_for_group(groups)

def clean_garbage(word):
  clean_word = ''
  i = 0
  if len(word) < 2:
    return word
  word = word[1:-1]
  while i < len(word):
    if word[i] == IGNORE_NEXT:
      i += 1
    else:
      clean_word += word[i]
    i += 1
  return clean_word
 
def count_valid_chars(word):
  return len(clean_garbage(word)) 

def get_num_non_cancelled_from_file():
  input_groups = ''
  with open('garbage') as f:
    input_groups += ''.join([row for row in f.readlines()])
  _, garbage = find_groups_in_string(input_groups)
  return sum([count_valid_chars(word) for word in garbage])
