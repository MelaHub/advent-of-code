import unittest
from ddt import ddt, data, unpack

from balancing import *

@ddt
class BalancingTest(unittest.TestCase):

  @data(
    ('pbga (66)', 'pbga', 66, []),
    ('fwft (72) -> ktlj, cntj, xhth', 'fwft', 72, ['ktlj', 'cntj', 'xhth'])
  )
  @unpack
  def test_parse_input(self, input_program, expected_name, expected_weight, expected_balancing):
    balanceTree = BalanceTree()
    name, weight, balancing = balanceTree._parse_program(input_program)
    self.assertEquals(name, expected_name)
    self.assertEquals(weight, expected_weight)
    self.assertEquals(balancing, expected_balancing)
