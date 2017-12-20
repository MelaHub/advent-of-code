def reverse_elements(input_list, current_position, length):
  copy_input = [e for e in input_list]
  end_position = current_position + length
  if end_position >= len(input_list):
    end_position -= len(input_list)
  i = current_position
  j = end_position - 1
  start_reverse = False
  while i != end_position or not start_reverse:
    start_reverse = True
    copy_input[i] = input_list[j]
    i += 1
    j -= 1
    if i == len(input_list):
      i = 0
    if j == -1:
      j = len(input_list) - 1
  return copy_input
    
