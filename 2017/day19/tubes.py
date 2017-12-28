from collections import namedtuple

VERTICAL_TUBE = '|'
HORIZONTAL_TUBE = '-'
CROSSROAD = '+'
UP = 'UP'
DOWN = 'DOWN'
LEFT = 'LEFT'
RIGHT = 'RIGHT'
EMPTY = ' '

Coordinate = namedtuple('Coordinate', ['row', 'col'])
Position = namedtuple('Position', ['coordinate', 'direction'])

def find_starting_point(grid):
  for i in range(len(grid[0])):
    if grid[0][i] == VERTICAL_TUBE:
      return Position(Coordinate(0, i), DOWN)
  raise Exception('No starting point found')

def init_tubes_from_file():
  grid = []
  with open('tubes') as f:
    grid += f.read().split('\n')
  return grid

def check_in_boundaries(coordinates, symbol, grid):
  return (coordinates.row >= 0 and coordinates.row < len(grid) and
    coordinates.col >= 0 and coordinates.col < len(grid[0]) and
    grid[coordinates.row][coordinates.col] != symbol and 
    grid[coordinates.row][coordinates.col] != EMPTY)

def move(current_position, grid):

  AlternativePositions = namedtuple('AlternativePositions', ['keep_going', 'first_alternative', 'second_alternative'])

  row, col = current_position.coordinate.row, current_position.coordinate.col
  current_direction = current_position.direction

  alternatives = None
  
  if current_direction == DOWN:
    alternatives = AlternativePositions(
      Position(Coordinate(row + 1, col), DOWN),
      Position(Coordinate(row, col - 1), LEFT),
      Position(Coordinate(row, col + 1), RIGHT)
    )
  elif current_direction == UP:
    alternatives = AlternativePositions(
      Position(Coordinate(row - 1, col), UP),
      Position(Coordinate(row, col - 1), LEFT),
      Position(Coordinate(row, col + 1), RIGHT)
    )
  elif current_direction == RIGHT:
    alternatives = AlternativePositions(
      Position(Coordinate(row, col + 1), RIGHT),
      Position(Coordinate(row - 1, col), UP),
      Position(Coordinate(row + 1, col), DOWN)
    )
  elif current_direction == LEFT:
    alternatives = AlternativePositions(
      Position(Coordinate(row, col - 1), LEFT),
      Position(Coordinate(row - 1, col), UP),
      Position(Coordinate(row + 1, col), DOWN)
    )
  next_movement = None
  if check_in_boundaries(current_position.coordinate, CROSSROAD, grid):
    next_movement = alternatives.keep_going
  else:
    if check_in_boundaries(alternatives.first_alternative.coordinate, EMPTY, grid):
      next_movement = alternatives.first_alternative
    elif check_in_boundaries(alternatives.second_alternative.coordinate, EMPTY, grid):
      next_movement = alternatives.second_alternative
  return next_movement

def follow_the_tubes(grid):
  curr_position = find_starting_point(grid)
  letters = ''
  number_of_steps = 0
  while curr_position != None:
    number_of_steps += 1
    curr_tube = grid[curr_position.coordinate.row][curr_position.coordinate.col]
    if curr_tube not in [CROSSROAD, VERTICAL_TUBE, HORIZONTAL_TUBE, EMPTY]:
      letters += curr_tube
    curr_position = move(curr_position, grid)
  return letters, number_of_steps - 1

def follow_the_tubes_from_file():
  grid = init_tubes_from_file()
  return follow_the_tubes(grid)
