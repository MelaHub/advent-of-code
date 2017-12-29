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
  return test_rules.get('/'.join(input_square)).split('/')
 
