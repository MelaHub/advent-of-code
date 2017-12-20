def reverse_elements(input_list, current_position, length):
  list_len = len(input_list)
  if current_position >= list_len:
    current_position -= list_len
  copy_input = [e for e in input_list]
  end_position = current_position + length
  if end_position >= list_len:
    end_position -= list_len
  i = current_position - 1
  j = end_position
  start_copy = False
  while i != j - 2:
    i += 1
    j -= 1
    if i == len(input_list):
      i = 0
    if j == -1:
      j = len(input_list) - 1
    if start_copy and (i == 0 and j == len(input_list) - 1 or i == j + 1):
      break
    copy_input[i], copy_input[j] = copy_input[j], copy_input[i]
    start_copy = True
  return copy_input
  
def reverse_for_each_length(input_list, lengths):
  another_list = [e for e in input_list]
  curr_position = 0
  skip_size = 0
  for length in lengths:
    if length > len(input_list):
      continue
    another_list = reverse_elements(input_list, curr_position, length)
    curr_position += (length + skip_size)
    skip_size += 1
