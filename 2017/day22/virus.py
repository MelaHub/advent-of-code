from collections import namedtuple

INFECTED_CELL = '#'
WEAKENED = 'W'
FLAGGED = 'F'
CLEAN_CELL = '.'
UP = 'UP'
DOWN = 'DOWN'
LEFT = 'LEFT'
RIGHT = 'RIGHT'

Coordinates = namedtuple('Coordinates', ['x', 'y', 'direction'])

class BasicVirus(object):

  current_position = None

  def __init__(self, coordinate):
    print 'Virus starts at position (%s, %s, %s)' % (coordinate.x, coordinate.y, coordinate.direction)
    self.current_position = coordinate


class Virus(BasicVirus):

  def move_and_infect(self, current_cell_status):
    new_status = None
    if current_cell_status == INFECTED_CELL:
      new_status = CLEAN_CELL
      if self.current_position.direction == UP:
        self.current_position = Coordinates(self.current_position.x + 1, self.current_position.y, RIGHT)
      elif self.current_position.direction == RIGHT:
        self.current_position = Coordinates(self.current_position.x, self.current_position.y + 1, DOWN)
      elif self.current_position.direction == DOWN:
        self.current_position = Coordinates(self.current_position.x - 1, self.current_position.y, LEFT)
      elif self.current_position.direction == LEFT:
        self.current_position = Coordinates(self.current_position.x, self.current_position.y - 1, UP)
    elif current_cell_status == CLEAN_CELL:
      if self.current_position.direction == UP:
        self.current_position = Coordinates(self.current_position.x - 1, self.current_position.y, LEFT)
      elif self.current_position.direction == RIGHT:
        self.current_position = Coordinates(self.current_position.x, self.current_position.y - 1, UP)
      elif self.current_position.direction == DOWN:
        self.current_position = Coordinates(self.current_position.x + 1, self.current_position.y, RIGHT)
      elif self.current_position.direction == LEFT:
        self.current_position = Coordinates(self.current_position.x, self.current_position.y + 1, DOWN)
      new_status = INFECTED_CELL
    return new_status


class StrongerVirus(BasicVirus):

  def move_and_infect(self, current_cell_status):
    raise NotImplementedError()


class ClusterMap(object):

  infected_cells = None
  virus = None
  number_of_caused_infections = None
 
  def __init__(self, initial_grid, virus):
    self.infected_cells = set()
    for i in range(len(initial_grid)):
      for j in range(len(initial_grid[i])):
        if initial_grid[j][i] == INFECTED_CELL:
          self.infected_cells.add((i, j))
    self.virus = virus
    self.number_of_caused_infections = 0

  def move_virus(self, number_turns):
    for i in range(number_turns):
      current_cell_status = CLEAN_CELL
      current_cell_virus = (self.virus.current_position.x, self.virus.current_position.y)
      if current_cell_virus in self.infected_cells:
        current_cell_status = INFECTED_CELL
      new_status = self.virus.move_and_infect(current_cell_status)
      if new_status == INFECTED_CELL:
        self.infected_cells.add(current_cell_virus)
        self.number_of_caused_infections += 1
      else:
        self.infected_cells.remove(current_cell_virus)
      

def init_grid(grid):
  virus = Virus(Coordinates(round(float(len(grid[0]) / 2)), round(float(len(grid) / 2)), UP))
  grid = ClusterMap(grid, virus)
  return grid

def get_grid_from_file():
  grid = []
  with open('virus') as f:
    grid += [row.strip() for row in f.readlines()]
  return grid
