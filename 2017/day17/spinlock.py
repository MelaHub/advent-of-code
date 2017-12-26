def spin(n_times, steps):
  circular_buffer = [0]
  position = 0
  for i in xrange(n_times):
    position = ((position + steps) % len(circular_buffer)) + 1
    circular_buffer = circular_buffer[:position] + [i + 1] + circular_buffer[position:]
  return circular_buffer
