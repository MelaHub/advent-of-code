import unittest
from ddt import ddt, data, unpack

from dueling import *

@ddt
class DefragTest(unittest.TestCase):

  @data(
    (65, lambda x: GeneratorA(x), [1092455, 1181022009, 245556042, 1744312007, 1352636452]),
    (8921, lambda x: GeneratorB(x), [430625591, 1233683848, 1431495498, 137874439, 285222916]),
  )
  @unpack
  def test_gen_next_value(self, start_value, get_generator, expected_values):
    gen = get_generator(start_value)
    values = []
    for i in range(0, 5):
      values.append(gen.gen_next())
    self.assertEquals(expected_values, values)
  
