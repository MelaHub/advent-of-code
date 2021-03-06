from collections import namedtuple

INFECTED_CELL = '#'
WEAKENED_CELL = 'W'
FLAGGED_CELL = 'F'
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

  def move_right(self):
    self.current_position = Coordinates(self.current_position.x + 1, self.current_position.y, RIGHT)

  def move_down(self):
    self.current_position = Coordinates(self.current_position.x, self.current_position.y + 1, DOWN)

  def move_left(self):
    self.current_position = Coordinates(self.current_position.x - 1, self.current_position.y, LEFT)

  def move_up(self):
    self.current_position = Coordinates(self.current_position.x, self.current_position.y - 1, UP)



class Virus(BasicVirus):

  def move_and_infect(self, current_cell_status):
    new_status = None
    if current_cell_status == INFECTED_CELL:
      new_status = CLEAN_CELL
      if self.current_position.direction == UP:
        self.move_right()
      elif self.current_position.direction == RIGHT:
        self.move_down()
      elif self.current_position.direction == DOWN:
        self.move_left()
      elif self.current_position.direction == LEFT:
        self.move_up()
    elif current_cell_status == CLEAN_CELL:
      if self.current_position.direction == UP:
        self.move_left()
      elif self.current_position.direction == RIGHT:
        self.move_up()
      elif self.current_position.direction == DOWN:
        self.move_right()
      elif self.current_position.direction == LEFT:
        self.move_down()
      new_status = INFECTED_CELL
    return new_status


class SuperVirus(BasicVirus):

  def move_and_infect(self, current_cell_status):
    new_status = None
    if current_cell_status == INFECTED_CELL:
      new_status = CLEAN_CELL
      if self.current_position.direction == UP:
        self.move_right()
      elif self.current_position.direction == RIGHT:
        self.move_down()
      elif self.current_position.direction == DOWN:
        self.move_left()
      elif self.current_position.direction == LEFT:
        self.move_up()
      new_status = FLAGGED_CELL
    elif current_cell_status == CLEAN_CELL:
      if self.current_position.direction == UP:
        self.move_left()
      elif self.current_position.direction == RIGHT:
        self.move_up()
      elif self.current_position.direction == DOWN:
        self.move_right()
      elif self.current_position.direction == LEFT:
        self.move_down()
      new_status = WEAKENED_CELL
    elif current_cell_status == WEAKENED_CELL:
      if self.current_position.direction == UP:
        self.move_up()
      elif self.current_position.direction == RIGHT:
        self.move_right()
      elif self.current_position.direction == DOWN:
        self.move_down()
      elif self.current_position.direction == LEFT:
        self.move_left()
      new_status = INFECTED_CELL
    elif current_cell_status == FLAGGED_CELL:
      if self.current_position.direction == UP:
        self.move_down()
      elif self.current_position.direction == RIGHT:
        self.move_left()
      elif self.current_position.direction == DOWN:
        self.move_up()
      elif self.current_position.direction == LEFT:
        self.move_right()
      new_status = CLEAN_CELL
    return new_status


class ClusterMap(object):

  infected_cells = None
  virus = None
  number_of_caused_infections = None
 
  def __init__(self, initial_grid, virus):
    self.infected_cells = {}
    for i in range(len(initial_grid)):
      for j in range(len(initial_grid[i])):
        self.infected_cells[(i, j)] = initial_grid[j][i]
    self.virus = virus
    self.number_of_caused_infections = 0

  def move_virus(self, number_turns):
    for i in range(number_turns):
      current_cell_virus = (self.virus.current_position.x, self.virus.current_position.y)
      new_status = self.virus.move_and_infect(self.infected_cells.get(current_cell_virus, CLEAN_CELL))
      self.infected_cells[current_cell_virus] = new_status
      if new_status == INFECTED_CELL:
        self.number_of_caused_infections += 1
      

def init_grid(grid, virus_type):
  virus = virus_type(Coordinates(round(float(len(grid[0]) / 2)), round(float(len(grid) / 2)), UP))
  grid = ClusterMap(grid, virus)
  return grid

def get_grid_from_file():
  grid = []
  with open('virus') as f:
    grid += [row.strip() for row in f.readlines()]
  return grid
