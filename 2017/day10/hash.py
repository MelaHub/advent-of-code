def reverse_elements(input_list, current_position, length):
  copy_input = [e for e in input_list]
  end_position = current_position + length
  if end_position >= len(input_list):
    end_position -= len(input_list)
  i = current_position
  j = end_position - 1
  while i != j - 1 or i != j - 2 or not (i == 0 and j == len(input_list) - 1):
    copy_input[i], copy_input[j] = copy_input[j], copy_input[i]
    i += 1
    j -= 1
    if i == len(input_list):
      i = 0
    if j == -1:
      j = len(input_list) - 1
  return copy_input
    
