from day10.hash import knot_hash

GRID_SIZE = 128

def knot_hash_to_binary_row(knot_hash):
  binary_repr = ''
  for hex_value in knot_hash:
    binary_repr += bin(int(hex_value, 16))[2:].zfill(4)
  return binary_repr

def input_to_knot(input_string):
  return knot_hash(range(256), input_string)

def generate_grid(input_string):
  rows = []
  for i in range(GRID_SIZE):
    knot_hash = input_to_knot('%s-%d' % (input_string, i))
    rows.append(knot_hash_to_binary_row(knot_hash))
  return rows
  
def get_number_of_used_squares(input_string):
  grid = generate_grid(input_string)
  return sum([
    int(j) for i in grid for j in i])

