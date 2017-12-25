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

NEIGHBORHOOD = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if abs(i) != abs(j)]

def merge_regions(i, j, square_size, full_grid):
  if square_size == 1:
    if full_grid[i][j] == '0':
      return [set()]
    else:
      return [set([(i, j)] + (
          [(x, y) for (x, y) in [(i + h, j + k) for (h, k) in NEIGHBORHOOD]
            if x >= 0 and x < GRID_SIZE and y >= 0 and y < GRID_SIZE and full_grid[x][y] == '1'])
        )]

  reduced_square_size = square_size / 2
  neighborhoods = []
  for x in [i, i + reduced_square_size]:
    for y in [j, j + reduced_square_size]:
      neighborhoods += merge_regions(x, y, reduced_square_size, full_grid)

  regions_to_check = [r for r in neighborhoods if len(r) > 0]
  regions = []
  while len(regions_to_check):
    region, regions_to_check = regions_to_check[0], regions_to_check[1:]
    is_new_region = True
    for r in [x for x in regions_to_check]:
      if len(region.intersection(r)):
        regions_to_check.remove(r)
        regions_to_check.append(r.union(region))
        is_new_region = False
    if is_new_region:
      regions.append(region)
  return regions

def get_number_of_regions_rec(input_string):
  grid = generate_grid(input_string)
  regions = merge_regions(0, 0, GRID_SIZE, grid)
  return len(regions)
