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
    balance_programs = BalancePrograms()
    name, weight, balancing = balance_programs._parse_program(input_program)
    self.assertEquals(name, expected_name)
    self.assertEquals(weight, expected_weight)
    self.assertEquals(balancing, expected_balancing)

  def test_insert_nodes(self):
    balance_programs = BalancePrograms()
    balance_programs.insert('pbga (66)')
    self.assertEquals(sorted(balance_programs.roots), ['pbga'])
    balance_programs.insert('fwft (72) -> ktlj, cntj, xhth')
    self.assertEquals(sorted(balance_programs.roots), ['fwft', 'pbga'])
    balance_programs.insert('padx (45) -> pbga, havc, qoyq')
    self.assertEquals(sorted(balance_programs.roots), ['fwft', 'padx'])
    balance_programs.insert('abcd (45) -> padx, fwft, xywz')
    self.assertEquals(sorted(balance_programs.roots), ['abcd'])
    balance_programs.insert('xywz (45)')
    self.assertEquals(sorted(balance_programs.roots), ['abcd'])

  def test_find_root(self):
    self.assertEquals(find_root_from_file(), set(['vmpywg']))
   
