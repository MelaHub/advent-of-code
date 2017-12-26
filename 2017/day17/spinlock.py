def new_position(position, steps, len_buffer):
    return ((position + steps) % len_buffer) + 1

def spin(n_times, steps):
  circular_buffer = [0]
  position = 0
  for i in xrange(n_times):
    position = new_position(position, steps, i + 1)
    circular_buffer = circular_buffer[:position] + [i + 1] + circular_buffer[position:]
  return circular_buffer

def check_position_at(n_times, steps, desired_target_position):
  position = 0
  value_at_position = None
  for i in xrange(n_times):
    position = new_position(position, steps, i + 1)
    if position == desired_target_position:
      value_at_position = i + 1
  return value_at_position
    
        

