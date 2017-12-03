from math import ceil, floor, sqrt

def get_memory_position(memory_location):
  square_size = ceil(sqrt(memory_location))
  if square_size % 2 == 0:
    square_size += 1
  min_square = pow(square_size - 2, 2) + 1
  max_square = pow(square_size, 2)
  square_coordinates = [
    (min_square + n * (square_size - 1), min_square + (n + 1) * (square_size - 1) - 1)
    for n in range(0, 4)
  ]
  coordinates = (0, 0)
  half_arm = floor(square_size / 2)
  for i, (min_arm, max_arm) in enumerate(square_coordinates):
    if memory_location >= min_arm and memory_location <= max_arm:
      position_on_arm = memory_location - min_arm - half_arm + 1
      if i == 0:
        coordinates = (half_arm, position_on_arm)
      elif i == 1:
        coordinates = (-position_on_arm, half_arm)
      elif i == 2:
        coordinates = (-half_arm, -position_on_arm)
      elif i == 3:
        coordinates = (position_on_arm, -half_arm)
      break
  return coordinates

def get_distance(x, y):
  return abs(x) + abs(y)

def manhattan_memory(memory_location):
  return get_distance(*(get_memory_position(memory_location)))

NEIGHBORHOOD = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if (x, y) != (0, 0)]

def _sum_adiacent_fn(more_than, coordinates):
  curr_index = len(coordinates.keys())
  (x_new, y_new) = get_memory_position(curr_index + 1)
  memory_value = sum([coordinates.get((x_new + x, y_new + y), 0)
    for (x, y) in NEIGHBORHOOD])
  if memory_value > more_than:
    return memory_value
  else:
    coordinates.update({(x_new, y_new): memory_value})
    return _sum_adiacent_fn(more_than, coordinates)
  
def sum_adiacent(more_than):
  return _sum_adiacent_fn(more_than, {(0, 0): 1})

