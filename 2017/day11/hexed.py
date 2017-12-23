# funzione che data coordinata e direzione mi ritorna la coordinata nuova
# funzione che legge una serie di coordinate e ritorna la coordinata finale
# funzione che date due coordinate calcola il minimo percorso

class HexTile():

  x = None
  y = None

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def move(self, direction):
    move_x, move_y = None, None
    if direction == 'nw':
      move_x, move_y = (-1, 1)
    elif direction == 'n':
      move_x, move_y = (0, 2)
    elif direction == 'ne':
      move_x, move_y = (1, 1)
    elif direction == 'se':
      move_x, move_y = (1, -1)
    elif direction == 's':
      move_x, move_y = (0, -2)
    elif direction == 'sw':
      move_x, move_y = (-1, -1)
    return HexTile(self.x + move_x, self.y + move_y)

  def __eq__(self, other):
    return self.x == other.x and self.y == other.y
