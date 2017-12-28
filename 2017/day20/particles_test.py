import unittest
from ddt import ddt, data, unpack

from particles import *

@ddt
class ParticlesTest(unittest.TestCase):

  TEST_PARTICLES = [
    'p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>',
    'p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>'
  ]

  @data(
    (TEST_PARTICLES[0], Coordinate(3, 0, 0), Coordinate(2, 0, 0), Coordinate(-1, 0, 0)),
    (TEST_PARTICLES[1], Coordinate(4, 0, 0), Coordinate(0, 0, 0), Coordinate(-2, 0, 0)),
  )
  @unpack
  def test_parse_input(self, input_string, expected_position, expected_velocity, expected_acceleration):
    self.assertEquals(Particle(expected_position, expected_velocity, expected_acceleration), parse_particle(input_string))

  @data(
    (parse_particle(TEST_PARTICLES[0]), [
      Particle(Coordinate(4, 0, 0), Coordinate(1, 0, 0), Coordinate(-1, 0, 0)),
      Particle(Coordinate(4, 0, 0), Coordinate(0, 0, 0), Coordinate(-1, 0, 0)),
      Particle(Coordinate(3, 0, 0), Coordinate(-1, 0, 0), Coordinate(-1, 0, 0))
    ]),
    (parse_particle(TEST_PARTICLES[1]), [
      Particle(Coordinate(2, 0, 0), Coordinate(-2, 0, 0), Coordinate(-2, 0, 0)),
      Particle(Coordinate(-2, 0, 0), Coordinate(-4, 0, 0), Coordinate(-2, 0, 0)),
      Particle(Coordinate(-8, 0, 0), Coordinate(-6, 0, 0), Coordinate(-2, 0, 0))
    ]),
  )
  @unpack
  def test_evolve(self, particle, expected_evolution):
    for expected_particle in expected_evolution:
      particle.evolve()
      self.assertEquals(expected_particle, particle)

  def test_distance(self):
    particle = parse_particle('p=< 3,4,5>, v=< 2,0,0>, a=<-1,0,0>')
    another_particle = parse_particle('p=<0,0,0>, v=<0,0,0>, a=<0,0,0>')
    self.assertEquals(12, particle.manhattan_distance(another_particle))
    
