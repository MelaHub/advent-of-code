import unittest
from ddt import ddt, data, unpack

from dueling import *

@ddt
class DefragTest(unittest.TestCase):

  @data(
    (65, lambda x: GeneratorAFirstHalf(x), [1092455, 1181022009, 245556042, 1744312007, 1352636452]),
    (8921, lambda x: GeneratorBFirstHalf(x), [430625591, 1233683848, 1431495498, 137874439, 285222916]),
  )
  @unpack
  def test_gen_next_value(self, start_value, get_generator, expected_values):
    gen = get_generator(start_value)
    values = []
    for i in range(0, 5):
      values.append(gen.gen_next())
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
    (65, 8921, 5, 1),
    # (65, 8921, 40000000, 588),
    # (277, 349, 40000000, 592),
  )
  @unpack
  def test_assert_correct_judgment(self, start_a, start_b, n_rounds, expected_rounds):
    judge = Judge([GeneratorAFirstHalf(start_a), GeneratorBFirstHalf(start_b)])
    self.assertEquals(expected_rounds, judge.judge(n_rounds))
