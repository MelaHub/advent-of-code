import unittest
from ddt import ddt, data, unpack

from scanner import *

@ddt
class PlumberTest(unittest.TestCase):

  SAMPLE_INPUT = [
    '0: 3',
    '1: 2',
    '4: 4',
    '6: 4'
  ]

  def test_parse_input(self):
    self.assertEquals(Laser(0, 3), parse_input('0: 3'))

  def test_build_scanner(self):
    scanner = build_scanner(self.SAMPLE_INPUT)
    self.assertEquals([0, 1, 4, 6], sorted(scanner.layers.keys()))
    self.assertEquals(Laser(3, 0), scanner[3])
    self.assertEquals(Laser(6, 4), scanner[6])

  def test_severity(self):
    self.assertEquals(24, Laser(6, 4).severity)

  def test_check_will_collide(self):
    scanner = build_scanner(self.SAMPLE_INPUT)
    self.assertEquals(True, scanner[0].will_collide(0))
    self.assertEquals(False, scanner[1].will_collide(1))
    self.assertEquals(False, scanner[2].will_collide(2))
    self.assertEquals(False, scanner[3].will_collide(3))
    self.assertEquals(False, scanner[4].will_collide(4))
    self.assertEquals(False, scanner[5].will_collide(5))
    self.assertEquals(True, scanner[6].will_collide(6))

  def test_total_severity(self):
    self.assertEquals(24, get_packet_severity(self.SAMPLE_INPUT))

  def test_total_severity_from_file(self):
    self.assertEquals(1588, get_packet_severity_from_file())

  def test_delay_packet(self):
    self.assertEquals(10, delay_packet(self.SAMPLE_INPUT))

  def test_delay_packet_from_file(self):
    self.assertEquals(3865118, delay_packet_from_file())
