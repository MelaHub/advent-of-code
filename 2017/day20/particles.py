import re
# test input
# test incremento next step particella

INPUT_PARTICLE = r'p=\<(?P<position>.*)\>, v=\<(?P<velocity>.*)\>, a=\<(?P<acceleration>.*)\>'

class Coordinate(object):
  x = None
  y = None
  z = None

  def __init__(self, x, y, z):
    self.x, self.y, self.z = x, y, z

  def __eq__(self, other):
    return self.x == other.x and self.y == other.y and self.z == other.z


class Particle(object):

  position = None
  velocity = None
  acceleration = None

  def __init__(self, position, velocity, acceleration):
    self.position = position
    self.velocity = velocity
    self.acceleration = acceleration

  def __eq__(self, other):
    return (self.position == other.position and 
      self.velocity == other.velocity and
      self.acceleration == other.acceleration)


def parse_input_to_coordinate(input_string):
  coordinates = [int(c.strip()) for c in input_string.split(',')]
  return Coordinate(*coordinates)


def parse_particle(input_string):
  parse_input = re.search(INPUT_PARTICLE, input_string)
  return Particle(parse_input_to_coordinate(parse_input.group('position')),
                  parse_input_to_coordinate(parse_input.group('velocity')),
                  parse_input_to_coordinate(parse_input.group('acceleration')))
