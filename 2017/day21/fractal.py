STARTING_PATTERN = [
  '.#.',
  '..#',
  '###'
]

def rotate_flip_square(input_square):
  rotatezip = lambda x: [''.join(e) for e in zip(*x[::-1])]
  rotate90 = rotatezip(input_square)
  rotate180 = rotatezip(rotate90)
  rotate270 = rotatezip(rotate180)
  return [input_square, rotate90, rotate180, rotate270, [row[::-1] for row in input_square]]

def replace_square(input_square, test_rules):
  rotated_flipped_input = rotate_flip_square(input_square)
  matching_output = None
  for square in rotated_flipped_input:
    match = test_rules.get('/'.join(square))
    if match is not None:
      matching_output = match
      break
  return matching_output.split('/')

def split_by_factor(input_square, factor):
  output_rows = []
  indexes = [i for i in range(0, len(input_square), factor)]
  for x, y in [(i, j) for i in indexes for j in indexes]:
    output_rows.append([row[y:y+factor] for row in input_square[x:x+factor]])
  return output_rows

def split_square(input_square):
  if len(input_square) == 2 or len(input_square) == 3:
    return input_square
  if len(input_square) % 2 == 0:
    return split_by_factor(input_square, 2)
  elif len(input_square) % 3 == 0:
    return split_by_factor(input_square, 3)
  return Exception('HEEEELP a weird square!!!')
