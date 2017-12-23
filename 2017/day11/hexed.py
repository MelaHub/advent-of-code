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

def follow_path(starting_point, string_path):
  path = string_path.split(',')
  position = starting_point
  for direction in path:
    position = position.move(direction)
  return position  
