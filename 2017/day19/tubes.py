from collections import namedtuple

VERTICAL_TUBE = '|'
HORIZONTAL_TUBE = '-'
CROSSROAD = '+'
UP = 'UP'
DOWN = 'DOWN'
LEFT = 'LEFT'
RIGHT = 'RIGHT'
EMPTY = ' '

def find_starting_point(grid):
  for i in range(len(grid[0])):
    if grid[0][i] == VERTICAL_TUBE:
      return (0, i), DOWN
  raise Exception('No starting point found')

def init_tubes_from_file():
  grid = []
  with open('tubes') as f:
    grid.append(f.read().split('\n'))
  return grid

Coordinate = namedtuple('Coordinate', ['row', 'col'])
Movement = namedtuple('Movement', ['coordinate', 'direction'])

def check_in_boundaries(coordinates, symbol, grid):
  return (coordinates.row >= 0 and coordinates.row < len(grid) and
    coordinates.col >= 0 and coordinates.col < len(grid[0]) and
    grid[coordinates.row][coordinates.col] != symbol)

def move(current_movement, grid):

  AlternativeMovements = namedtuple('AlternativeMovements', ['keep_going', 'first_alternative', 'second_alternative'])

  row, col = current_movement.coordinate.row, current_movement.coordinate.col
  current_direction = current_movement.direction

  alternatives = None
  
  if current_direction == DOWN:
    alternatives = AlternativeMovements(
      Movement(Coordinate(row + 1, col), DOWN),
      Movement(Coordinate(row, col - 1), LEFT),
      Movement(Coordinate(row, col + 1), RIGHT)
    )
  elif current_direction == UP:
    alternatives = AlternativeMovements(
      Movement(Coordinate(row - 1, col), UP),
      Movement(Coordinate(row, col - 1), LEFT),
      Movement(Coordinate(row, col + 1), RIGHT)
    )
  elif current_direction == RIGHT:
    alternatives = AlternativeMovements(
      Movement(Coordinate(row, col + 1), RIGHT),
      Movement(Coordinate(row - 1, col), UP),
      Movement(Coordinate(row + 1, col), DOWN)
    )
  elif current_direction == LEFT:
    alternatives = AlternativeMovements(
      Movement(Coordinate(row, col - 1), LEFT),
      Movement(Coordinate(row - 1, col), UP),
      Movement(Coordinate(row + 1, col), DOWN)
    )
  next_movement = None
  if check_in_boundaries(current_movement.coordinate, CROSSROAD, grid):
    next_movement = alternatives.keep_going
  else:
    if check_in_boundaries(alternatives.first_alternative.coordinate, EMPTY, grid):
      next_movement = alternatives.first_alternative
    elif check_in_boundaries(alternatives.second_alternative.coordinate, EMPTY, grid):
      next_movement = alternatives.second_alternative
  return next_movement
    
