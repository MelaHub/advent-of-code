STANDARD_LENGTHS = [17, 31, 73, 47, 23]
NUMBER_OF_ROUNDS = 64
BLOCK_SIZE = 16

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
  
def reverse_for_each_length(input_list, lengths, curr_position = 0, skip_size = 0):
  another_list = [e for e in input_list]
  for length in lengths:
    if length > len(input_list):
      continue
    another_list = reverse_elements(another_list, curr_position, length)
    curr_position = (curr_position + length + skip_size) % len(another_list)
    skip_size += 1
  return another_list, curr_position, skip_size

def knot_list(input_list, lengths):
  reversed_list, _, _ = reverse_for_each_length(input_list, lengths)
  return reversed_list[0] * reversed_list[1]

def knot_hash(input_list, ascii_lengths):
  lengths = get_standard_lengths(ascii_lengths)
  sparse_hash = get_sparse_hash(input_list, lengths) 
  dense_hash = get_dense_hash(sparse_hash)
  return get_hex_hash(dense_hash)

def convert_to_ascii(input_string):
  return [ord(i) for i in input_string]

def get_standard_lengths(input_string):
  return convert_to_ascii(input_string) + STANDARD_LENGTHS

def get_sparse_hash(input_string, lengths):
  copy_list = [i for i in input_string]
  curr_position = 0
  skip_size = 0
  for i in range(0, NUMBER_OF_ROUNDS):
    copy_list, curr_position, skip_size = reverse_for_each_length(copy_list, lengths, curr_position, skip_size)
  return copy_list

def get_block_dense_hash(input_numbers):
  if len(input_numbers) != BLOCK_SIZE:
    raise Exception('Expected block size is %d' % BLOCK_SIZE)
  dense_hash = 0
  for n in input_numbers:
    dense_hash = dense_hash ^ n
  return dense_hash

def get_dense_hash(input_numbers):
  dense_hash = []
  for block_start in range(0, len(input_numbers), BLOCK_SIZE):
    dense_hash.append(get_block_dense_hash(input_numbers[block_start:block_start + BLOCK_SIZE]))
  return dense_hash

def get_hex_hash(input_numbers):
  return ''.join([hex(n).replace('0x', '').zfill(2) for n in input_numbers])
    
