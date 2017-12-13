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
    balancePrograms = BalancePrograms()
    name, weight, balancing = balancePrograms._parse_program(input_program)
    self.assertEquals(name, expected_name)
    self.assertEquals(weight, expected_weight)
    self.assertEquals(balancing, expected_balancing)

  def test_insert_nodes(self):
    balancePrograms = BalancePrograms()
    balancePrograms.insert('pbga (66)')
    self.assertEquals(sorted(balancePrograms.roots), ['pbga'])
    balancePrograms.insert('fwft (72) -> ktlj, cntj, xhth')
    self.assertEquals(sorted(balancePrograms.roots), ['fwft', 'pbga'])
    balancePrograms.insert('padx (45) -> pbga, havc, qoyq')
    self.assertEquals(sorted(balancePrograms.roots), ['fwft', 'padx'])
    balancePrograms.insert('abcd (45) -> padx, fwft')
    self.assertEquals(sorted(balancePrograms.roots), ['abcd'])
   
