STANDARD_LENGTHS = [17, 31, 73, 47, 23]
NUMBER_OF_ROUNDS = 64

def reverse_elements(input_list, current_position, length):
  list_len = len(input_list)
  copy_input = [e for e in input_list]
  if not length:
    return copy_input
  switch_elements_list = [(i % list_len, j % list_len)
    for (i, j) in zip(
      range(current_position, current_position + length / 2),
      range(current_position + length - 1, current_position + length / 2 - 1, -1))]
  for (i, j) in switch_elements_list:
    copy_input[i], copy_input[j] = copy_input[j], copy_input[i]
  return copy_input
  
def reverse_for_each_length(input_list, lengths):
  another_list = [e for e in input_list]
  curr_position = 0
  skip_size = 0
  for length in lengths:
    if length > len(input_list):
      continue
    another_list = reverse_elements(another_list, curr_position, length)
    curr_position = (curr_position + length + skip_size) % len(another_list)
    skip_size += 1
  return another_list

def knot_list(input_list, lengths):
  reversed_list = reverse_for_each_length(input_list, lengths)
  return reversed_list[0] * reversed_list[1]

def knot_hash(input_string):
  return input_string

def convert_to_ascii(input_string):
  return [ord(i) for i in input_string]

def get_standard_lengths(input_string):
  return convert_to_ascii(input_string) + STANDARD_LENGTHS
