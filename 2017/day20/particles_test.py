import unittest
from ddt import ddt, data, unpack

from particles import *

@ddt
class ParticlesTest(unittest.TestCase):

  @data(
    ('p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>', Coordinate(3, 0, 0), Coordinate(2, 0, 0), Coordinate(-1, 0, 0)),
    ('p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>', Coordinate(4, 0, 0), Coordinate(0, 0, 0), Coordinate(-2, 0, 0)),
  )
  @unpack
  def test_parse_input(self, input_string, expected_position, expected_velocity, expected_acceleration):
    self.assertEquals(Particle(expected_position, expected_velocity, expected_acceleration), parse_particle(input_string))

