class Laser():

  layer = None
  depth = None

  def __init__(self, layer, depth):
    self.layer, self.depth = layer, depth

  def __eq__(self, other):
    return self.layer == other.layer and self.depth == other.depth

  def __str__(self):
    return 'Laser(%d, %d)' % (self.layer, self.depth)

  @property
  def severity(self):
    return self.layer * self.depth

  def will_collide(self, t):
    if self.depth == 0:
      return False
    return self.position_at_time(t) == 0

  def position_at_time(self, t):
    return t % (self.depth + self.depth - 2)


class Scanner():

  layers = {}

  @property
  def last_layer(self):
    return max(self.layers.keys())

  def add_laser(self, laser):
    self.layers[laser.layer] = laser

  def print_status_at(self, time, packet_on_column):
    header = ''.join([' %s' % str(i).zfill(2) for i in range(self.last_layer + 1) if i < 31])
    n_rows = max([l.depth for l in self.layers.values()])
    rows = []
    for i in range(n_rows + 1):
      curr_row = ''
      for j in range(self.last_layer + 1):
        if i == 0 and packet_on_column == j:
          if self[j].depth > 0 and self[j].position_at_time(time) == i:
            curr_row += '(X)'
          else:
            curr_row += '( )'
        elif i < self[j].depth:
          if self[j].position_at_time(time) == i or self[j].position_at_time(time) >= self[j].depth and self[j].position_at_time(time) == (i + (self[j].position_at_time(time) - self[j].depth + 1) * 2):
            curr_row += '[X]'
          else:
            curr_row += '[ ]'
        else:
          curr_row += '...'
	if j >= 30:
          break
      rows.append(curr_row)
    return '\n'.join([header] + rows)

  def __getitem__(self, item):
    return self.layers.get(item, Laser(item, 0))


def parse_input(input_layers):
  layer, depth = input_layers.split(':')
  return Laser(int(layer), int(depth.strip()))


def build_scanner(input_layers):
  scanner = Scanner()
  for layer in input_layers:
    scanner.add_laser(parse_input(layer))
  return scanner

def get_packet_severity(input_layers):
  scanner = build_scanner(input_layers)
  severity = 0
  for i in range(scanner.last_layer + 1):
    if scanner[i].will_collide(i):
      severity += scanner[i].severity
  return severity

def _get_layers_from_file():
  input_layers = []
  with open('scanner') as f:
    input_layers += [row.strip() for row in f.readlines()]
  return input_layers

def get_packet_severity_from_file():
  input_layers = _get_layers_from_file()
  return get_packet_severity(input_layers)

def delay_packet(input_layers):
  scanner = build_scanner(input_layers)
  collides = True
  delay = -1
  while collides:
    delay += 1
    if delay % 2 == 1: # collides always with 1
      continue
    print 'Check if packet collides with a delay of %d ps' % delay
    curr_delay_collides = False
    for i in range(scanner.last_layer + 1):
      # print '=======================> TIME %d\n%s' % (delay + i, scanner.print_status_at(delay + i, i))
      # raw_input()
      if scanner[i].will_collide(delay + i):
        curr_delay_collides = True
        break
    collides = curr_delay_collides
  return delay

def delay_packet_from_file():
  input_layers = _get_layers_from_file()
  return delay_packet(input_layers)
    
    
