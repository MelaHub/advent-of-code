import re
import math

INPUT_PARTICLE = r'p=\<(?P<position>.*)\>, v=\<(?P<velocity>.*)\>, a=\<(?P<acceleration>.*)\>'

class Coordinate(object):
  x = None
  y = None
  z = None

  def __init__(self, x, y, z):
    self.x, self.y, self.z = float(x), float(y), float(z)

  def __eq__(self, other):
    return self.x == other.x and self.y == other.y and self.z == other.z

  def __str__(self):
    return '%d, %d, %d' % (self.x, self.y, self.z)

  def sum(self, other):
    return Coordinate(self.x + other.x, self.y + other.y, self.z + other.z)

  def diff(self, other):
    return Coordinate(self.x - other.x, self.y - other.y, self.z - other.z)

  def distance_from_origin(self):
    return abs(self.x) + abs(self.y) + abs(self.z)

  def distance(self, other):
    return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)

  def divide(self, value):
    return Coordinate(self.x / value, self.y / value, self.z / value)

  def to_tuple(self):
    return (self.x, self.y, self.z)


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
    self.velocity = self.velocity.sum(self.acceleration)
    self.position = self.position.sum(self.velocity)

  def manhattan_distance(self, other):
    return self.position.distance(other.position)

  def solve_equation(self, a, b, c):
    if a == 0:
      if b == 0:
        return []
      else:
        return [-c / b]
    delta = b * b - 4 * a * c
    if delta < 0:
      return []
    elif delta == 0:
      return [-b / (2 * a)]
    else:
      num = math.sqrt(delta)
      return [(-b - num) / (2 * a), (-b + num) / (2 * a)]

  def will_collide_on(self, other):
    acc_diff = other.acceleration.diff(self.acceleration)
    vel_diff = other.velocity.diff(self.velocity)
    pos_diff = other.position.diff(self.position)
    a_xyz = acc_diff.divide(2).to_tuple()
    b_xyz = vel_diff.sum(acc_diff.divide(2)).to_tuple()
    c_xyz = pos_diff.to_tuple()
    collision_at = [self.solve_equation(a, b, c) 
      for i, (a, b, c) in enumerate(zip(a_xyz, b_xyz, c_xyz))
      if pos_diff.to_tuple()[i] != 0
    ]
    integer_collisions_xyz = [[int(t) for t in collision_xyz if t.is_integer() and t >= 0] for collision_xyz in collision_at if collision_xyz is not None]
    integer_collisions = set()
    if len(integer_collisions_xyz):
      integer_collisions = set(integer_collisions_xyz[0])
      for t in integer_collisions_xyz[1:]:
        integer_collisions = integer_collisions.intersection(set(t))
    return list(integer_collisions)

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
  origin = Coordinate(0, 0, 0)
  min_property = min([get_property_from_particle(particle).distance(origin) for _, particle in particles])
  return [(i, particle) for (i, particle) in particles if get_property_from_particle(particle).distance(origin) == min_property]

def closest_to_origin(particles):
  particles_with_min_acc = get_min_in_collection(lambda x: x.acceleration, [(i, particle) for (i, particle) in enumerate(particles)])
  particles_with_min_vel = get_min_in_collection(lambda x: x.velocity, particles_with_min_acc)
  particles_with_min_pos = get_min_in_collection(lambda x: x.position, particles_with_min_vel)
  return particles_with_min_pos

def closest_to_origin_from_file():
  return closest_to_origin(particles_from_file())

def collisions_safe(particles):
  collisions_time = []
  for i in range(len(particles) - 1):
    for j in range(i + 1, len(particles)):
      collision_on = particles[i].will_collide_on(particles[j])
      if len(collision_on):
        collisions_time.append((particles[i], particles[j], collision_on))
  not_colliding_particles = [p for p in particles]
  t = min([t for _, _, times in collisions_time for t in times])
  t = 0
  while len(collisions_time):
    colliding_particles = set()
    for particle1, particle2, collision_on in collisions_time:
      if t in collision_on:
        colliding_particles.add(particle1)
        colliding_particles.add(particle2)
    for particle in colliding_particles:
      not_colliding_particles.remove(particle)
    collisions_time = [(p1, p2, time) 
      for (p1, p2, time) in collisions_time 
      if p1 not in colliding_particles and p2 not in colliding_particles]
    t += 1
  return not_colliding_particles

def collisions_safe_from_file():
  return collisions_safe(particles_from_file())

def collisions_evolution(particles):
  live_particles = [p for p in particles]
  t = 0
  last_change_t = 0
  while True:
    colliding_particles = set()
    for i in range(len(live_particles) - 1):
      for j in range(i + 1, len(live_particles)):
        if live_particles[i].manhattan_distance(live_particles[j]) == 0:
          colliding_particles.add(live_particles[i])
          colliding_particles.add(live_particles[j])
    live_particles = [p for p in live_particles if p not in colliding_particles]
    for p in live_particles:
      p.evolve()
    if len(colliding_particles):
      last_change_t = t
    if t - last_change_t > 30:
      break
    t += 1
  return live_particles
          
def collisions_evolution_from_file():
  return collisions_evolution(particles_from_file())
