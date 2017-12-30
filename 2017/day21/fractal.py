import math
STARTING_SQUARE = [
  '.#.',
  '..#',
  '###'
]

def rotate_flip_square(input_square):
  rotatezip = lambda x: [''.join(e) for e in zip(*x[::-1])]
  rotate90 = rotatezip(input_square)
  rotate180 = rotatezip(rotate90)
  rotate270 = rotatezip(rotate180)
  v_flip = [row[::-1] for row in input_square]
  h_flip = [row for row in input_square[::-1]]
  v_h_flip = [row[::-1] for row in h_flip]
  transpose_single = [input_square[j][i] for i in range(len(input_square) - 1, -1, -1) for j in range(len(input_square) - 1, -1, -1)]
  transpose = [''.join(transpose_single[k:k+len(input_square)]) for k in range(0, len(transpose_single), len(input_square))]
  return [input_square, rotate90, rotate180, rotate270, v_flip, h_flip, v_h_flip, transpose, [row for row in rotate270[::-1]]]

def replace_square(input_square, sub_rules):
  match = sub_rules.get('/'.join(input_square))
  if match is not None:
    return match.split('/')
  raise Exception('Couldn\'t find a match fo %s' % '/'.join(input_square))

def enrich_rules(input_rules):
  enriched_rules = {i: j for i, j in input_rules.iteritems()}
  for key, value in enriched_rules.items():
    flipped_keys = rotate_flip_square(key.split('/'))
    for flipped_key in flipped_keys:
      enriched_rules['/'.join(flipped_key)] = value
  return enriched_rules

def split_by_factor(input_square, factor):
  output_rows = []
  indexes = [i for i in range(0, len(input_square), factor)]
  for x, y in [(i, j) for i in indexes for j in indexes]:
    output_rows.append([row[y:y+factor] for row in input_square[x:x+factor]])
  return output_rows

def split_square(input_square):
  if len(input_square) == 2 or len(input_square) == 3:
    return [input_square]
  if len(input_square) % 2 == 0:
    return split_by_factor(input_square, 2)
  elif len(input_square) % 3 == 0:
    return split_by_factor(input_square, 3)
  return Exception('HEEEELP a weird square!!!')

def merge(squares):
  if len(squares) == 1:
    return squares[0]
  square_size = math.sqrt(len(squares) * len(squares[0] * len(squares[0][0])))
  blocks_per_row = int(square_size / len(squares[0][0]))
  grouped_blocks = zip(*[squares[i:i+blocks_per_row] for i in range(0, len(squares), blocks_per_row)])
  merge_grouped_blocks = []
  for group in grouped_blocks:
    merge_group = []
    for g in group:
      merge_group += g
    merge_grouped_blocks.append(merge_group)
  output_square = [''.join(group) for group in zip(*merge_grouped_blocks)]
  return output_square

def draw_fractal(input_square, round_left, sub_rules):
  enriched_rules = enrich_rules(sub_rules)
  if round_left == 0:
    return input_square
  sub_squares = split_square(input_square)
  new_squares = [replace_square(square, enriched_rules) for square in sub_squares]
  merged_squares = merge(new_squares)
  return draw_fractal(merged_squares, round_left - 1, sub_rules)
 
def count_pixels_on(round_left, sub_rules):
  a = draw_fractal(STARTING_SQUARE, round_left, sub_rules)
  return len([c for square in draw_fractal(STARTING_SQUARE, round_left, sub_rules) for row in square for c in row if c == '#']) 

def rules_from_file():
  rules = {}
  with open('fractal') as f:
    rules = {i.strip(): j.strip() for i, j in [row.split('=>') for row in f.readlines()]}
  return rules

def count_pixels_on_from_file(number_of_rounds):
  return count_pixels_on(number_of_rounds, rules_from_file())

