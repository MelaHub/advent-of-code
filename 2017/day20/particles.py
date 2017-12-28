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

  def __str__(self):
    return '%d, %d, %d' % (self.x, self.y, self.z)

  def sum(self, other):
    self.x += other.x
    self.y = other.y
    self.z = other.z

  def distance(self, other):
    return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)


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

  def __str__(self):
    return 'p=<%s>, v=<%s>, a=<%s>' % (self.position, self.velocity, self.acceleration)

  def evolve(self):
    self.velocity.sum(self.acceleration)
    self.position.sum(self.velocity)

  def manhattan_distance(self, other):
    return self.position.distance(other.position)


def parse_input_to_coordinate(input_string):
  coordinates = [int(c.strip()) for c in input_string.split(',')]
  return Coordinate(*coordinates)


def parse_particle(input_string):
  parse_input = re.search(INPUT_PARTICLE, input_string)
  return Particle(parse_input_to_coordinate(parse_input.group('position')),
                  parse_input_to_coordinate(parse_input.group('velocity')),
                  parse_input_to_coordinate(parse_input.group('acceleration')))

def particles_from_file():
  particles = []
  with open('particles') as f:
    particles += [parse_particle(row.strip()) for row in f.readlines()]
  return particles

def get_min_in_collection(get_property_from_particle, particles):
  min_property = min([get_property_from_particle(particle).distance(origin) for _, particle in particles])
  return [(i, particle) for (i, particle) in particles if get_property_from_particle(particle_.distance(origin) == min_property]

def closest_to_origin(particles):
  origin = Coordinate(0, 0, 0)
  particles_with_min_acc = get_min_in_collection(lambda x: x.acceleration, enumerate(particles))
  particles_with_min_vel = get_min_in_collection(lambda x: x.velocity, particles_with_min_acc)
  particles_with_min_pos = get_min_in_collection(lambda x: x.position, particles_with_min_vel)
   
  #  min_acc = min([particle.acceleration.distance(origin) for particle in particles])
  #  particles_with_min_acc = [particle for particle in particles
  #                            if particle.acceleration.distance(origin) == min_acc]
  #  min_velocity = min([particle.velocity.distance(origin) for particle in particles_with_min_acc])
  #  particles_with_min_vel = [particle for particle in particles_with_min_acc
  #                            if particle.velocity.distance(origin) == min_velocity]
  #  min_pos = min([particle.position.distance(origin) for particle in particles_with_min_vel])
  #  particles_with_min_pos = [particle for particle in particles_with_min_vel
  #                            if particle.position.distance(origin) == min_pos]
  return particles_with_min_pos
  


  
