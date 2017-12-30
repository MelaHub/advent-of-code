from collections import namedtuple

INFECTED_CELL = '#'
CLEAN_CELL = '.'
UP = 'UP'
DOWN = 'DOWN'
LEFT = 'LEFT'
RIGHT = 'RIGHT'

Coordinates = namedtuple('Coordinates', ['x', 'y', 'direction'])

class Virus(object):

  current_position = None

  def __init__(self, coordinate):
    print 'Virus starts at position (%s, %s, %s)' % (coordinate.x, coordinate.y, coordinate.direction)
    self.current_position = coordinate

  def move_and_infect(self, current_cell_status):
    new_status = None
    if current_cell_status == INFECTED_CELL:
      new_status = CLEAN_CELL
      if self.current_position.direction == UP:
        self.current_position = Coordinates(self.current_position.x + 1, self.current_position.y, RIGHT)
      elif self.current_position.direction == RIGHT:
        self.current_position = Coordinates(self.current_position.x, self.current_position.y - 1, DOWN)
      elif self.current_position.direction == DOWN:
        self.current_position = Coordinates(self.current_position.x - 1, self.current_position.y, LEFT)
      elif self.current_position.direction == LEFT:
        self.current_position = Coordinates(self.current_position.x, self.current_position.y + 1, UP)
    elif current_cell_status == CLEAN_CELL:
      if self.current_position.direction == UP:
        self.current_position = Coordinates(self.current_position.x - 1, self.current_position.y, LEFT)
      elif self.current_position.direction == RIGHT:
        self.current_position = Coordinates(self.current_position.x, self.current_position.y + 1, UP)
      elif self.current_position.direction == DOWN:
        self.current_position = Coordinates(self.current_position.x + 1, self.current_position.y, RIGHT)
      elif self.current_position.direction == LEFT:
        self.current_position = Coordinates(self.current_position.x, self.current_position.y - 1, DOWN)
      new_status = INFECTED_CELL
    return new_status

class ClusterMap(object):

  infected_cells = None
  virus = None
 
  def __init__(self, initial_grid, virus):
    self.infected_cells = set()
    for i in range(len(initial_grid)):
      for j in range(len(initial_grid[i])):
        if initial_grid[j][i] == INFECTED_CELL:
          self.infected_cells.add((j, i))
    self.virus = virus

def init_grid(grid):
  virus = Virus(Coordinates(round(float(len(grid[0]) / 2)), round(float(len(grid) / 2)), UP))
  grid = ClusterMap(grid, virus)
  return grid
