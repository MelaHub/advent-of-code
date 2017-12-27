VERTICAL_TUBE = '|'
HORIZONTAL_TUBE = '-'
CROSSROAD = '+'

def find_starting_point(grid):
  for i in range(len(grid[0])):
    if grid[0][i] == VERTICAL_TUBE:
      return (0, i)
  raise Exception('No starting point found')
