import unittest
from ddt import ddt, data, unpack

from dueling import *

@ddt
class DefragTest(unittest.TestCase):

  @data(
    (65, lambda x: GeneratorAFirstHalf(x), [1092455, 1181022009, 245556042, 1744312007, 1352636452]),
    (8921, lambda x: GeneratorBFirstHalf(x), [430625591, 1233683848, 1431495498, 137874439, 285222916]),
    (65, lambda x: GeneratorASecondHalf(x), [1352636452, 1992081072, 530830436, 1980017072, 740335192]),
    (8921, lambda x: GeneratorBSecondHalf(x), [1233683848, 862516352, 1159784568, 1616057672, 412269392]),
  )
  @unpack
  def test_gen_next_value(self, start_value, get_generator, expected_values):
    gen = get_generator(start_value)
    generator = gen.gen_next()
    i = 0
    values = []
    while i < 5:
      values.append(generator.next())
      i += 1
    self.assertEquals(expected_values, values)

  @data(
    ([1092455, 430625591], False),
    ([1181022009, 1233683848], False),
    ([245556042, 1431495498], True),
    ([1744312007, 137874439], False),
    ([1352636452, 285222916], False),
  )
  @unpack
  def test_are_statuses_equal(self, input_values, expected_judgment):
    self.assertEquals(expected_judgment, Judge([]).are_statuses_equal(input_values))

  @data(
    ([GeneratorAFirstHalf(65), GeneratorBFirstHalf(8921)], 5, 1),
    ([GeneratorAFirstHalf(65), GeneratorBFirstHalf(8921)], 40000000, 588),
    ([GeneratorAFirstHalf(277), GeneratorBfirstHalf(349)], 40000000, 592),
    ([GeneratorASecondHalf(65), GeneratorBSecondHalf(8921)], 5000000, 309),
    ([GeneratorASecondHalf(277), GeneratorBSecondHalf(349)], 5000000, 320),
  )
  @unpack
  def test_assert_icorrect_judgment(self, input_generators, n_rounds, expected_rounds):
    judge = Judge(input_generators)
    self.assertEquals(expected_rounds, judge.judge(n_rounds))

