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

def split_in_four(input_square):
  if len(input_square) == 2 or len(input_square) == 3:
    return input_square
