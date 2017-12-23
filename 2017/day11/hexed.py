# funzione che legge una serie di coordinate e ritorna la coordinata finale
# funzione che date due coordinate calcola il minimo percorso

NE = 'ne'
N = 'n'
NW = 'nw'
SW = 'sw'
S = 's'
SE = 'se'

class HexTile():

  x = None
  y = None

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def move(self, direction):
    move_x, move_y = None, None
    if direction == NW:
      move_x, move_y = (-1, 1)
    elif direction == N:
      move_x, move_y = (0, 2)
    elif direction == NE:
      move_x, move_y = (1, 1)
    elif direction == SE:
      move_x, move_y = (1, -1)
    elif direction == S:
      move_x, move_y = (0, -2)
    elif direction == SW:
      move_x, move_y = (-1, -1)
    return HexTile(self.x + move_x, self.y + move_y)

  def __eq__(self, other):
    return self.x == other.x and self.y == other.y

  def is_in_diagonal_with(self, other):
    return abs(self.x) - abs(other.x) == abs(self.y) - abs(other.y)

  def is_on_same_x_axis(self, other):
    return abs(abs(self.y) - abs(other.y)) < 2

  def is_norther(self, other):
    return self.y > other.y

  def is_souther(self, other):
    return self.y < other.y

  def copy(self):
    return HexTile(self.x, self.y)


def follow_path(starting_point, string_path):
  path = string_path.split(',')
  position = starting_point
  for direction in path:
    position = position.move(direction)
  return position

def _move_point(check_point, move_to, starting_point, ending_point):
  middle_point = starting_point.copy()
  path = 0
  if not middle_point.is_in_diagonal_with(ending_point) and check_point(middle_point, ending_point):
    n_moves = abs(abs(middle_point.y) - abs(ending_point.y)) / 2
    for i in range(n_moves):
      middle_point = middle_point.move(S)
    path += n_moves
  return middle_point, path
  

def find_shortest_path(starting_point, ending_point):
  middle_point = starting_point.copy()
  path_length = 0
  middle_point, moves_south = _move_point(lambda x, y: x.is_norther(y), S, middle_point, ending_point)
  middle_point, moves_north = _move_point(lambda x, y: x.is_souther(y), N, middle_point, ending_point)
  path_length += moves_south
  path_length += moves_north
  while not (middle_point.is_in_diagonal_with(ending_point) or not middle_point == ending_point):
    move = None
    if middle_point.x > ending_point.x:
      if middle_point.y > ending_point.y:
        move = SW
      elif middle_point.y < ending_point.y:
        move = NW
    elif middle_point.x < ending_point.x:
      if middle_point.y > ending_point.y:
        move = SE
      elif middle_point.y < ending_point.y:
        move = NE
    if move is not None:
      middle_point = middle_point.move(move)
      path_length += 1
  path_length += abs(abs(middle_point.x) - abs(ending_point.x))
  return path_length
