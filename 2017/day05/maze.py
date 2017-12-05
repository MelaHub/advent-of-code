def move_in_maze(maze, curr_index):
  next_index = curr_index + maze[curr_index]
  maze[curr_index] += 1
  return (maze, next_index)

# The recursive solutino is not feasible bcs of max level of recursion reached
def solve_maze_rec(maze, curr_index, number_of_moves):
  if curr_index < 0 or curr_index >= len(maze):
    return number_of_moves
  new_maze, next_index = move_in_maze(maze, curr_index)
  return solve_maze_rec(new_maze, next_index, number_of_moves + 1)    

def solve_maze(maze):
  number_of_moves = solve_maze_rec(maze, 0, 0)
  return number_of_moves

def solve_maze_non_rec(maze):
  curr_index = 0
  number_of_moves = 0
  while curr_index >= 0 and curr_index < len(maze):
    maze, curr_index = move_in_maze(maze, curr_index)
    number_of_moves += 1
  return number_of_moves

def solve_maze_from_file():
  rows = []
  with open('maze') as f:
    rows += [int(row) for row in f.readlines()]
  return solve_maze_non_rec(rows)
  
