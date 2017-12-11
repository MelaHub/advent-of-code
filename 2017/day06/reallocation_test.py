import unittest
from ddt import ddt, data, unpack

from reallocation import *

@ddt
class ReallocationTest(unittest.TestCase):

  @data(
    ([[0, 2, 7, 0]], {0: {2: {7: {0: 0}}}}),
    ([[0, 2, 7, 0], [0, 2, 1, 6]], {0: {2: {1: {6: 1}, 7: {0: 0}}}}),
  )
  @unpack
  def test_insert_in_memory_works(self, input_memory, expected_dict):
    memory_reallocator = MemoryReallocator(input_memory[0])
    for mem in input_memory[1:]:
      memory_reallocator._insert_in_memory(mem)
    self.assertEquals(memory_reallocator.memory, expected_dict)

  @data(
    ([0, 2, 1, 6], 1),
    ([0, 2, 1], -1),
    ([0, 2, 1, 6, 7], -1),
    ([0, 1], -1),
  )
  @unpack
  def test_find_in_memory(self, find_blocks, expected_outcome):
    memory_reallocator = MemoryReallocator([0, 2, 7, 0])
    memory_reallocator._insert_in_memory([0, 2, 1, 6])
    self.assertEquals(memory_reallocator._find_in_memory(find_blocks), expected_outcome)

  @data(
    ([0, 2, 7, 0], [2, 4, 1, 2]),
    ([2, 4, 1, 2], [3, 1, 2, 3]),
    ([3, 1, 2, 3], [0, 2, 3, 4]),
    ([0, 2, 3, 4], [1, 3, 4, 1]),
    ([1, 3, 4, 1], [2, 4, 1, 2]),
  )
  @unpack
  def test_one_step(self, input_values, expected_out):
    memory_reallocator = MemoryReallocator(input_values)
    self.assertEquals(memory_reallocator._one_step(input_values), expected_out)

  @data(
    ([0, 2, 7, 0], 5, [2, 4, 1, 2]),
    ([10, 3, 15, 10, 5, 15, 5, 15, 9, 2, 5, 8, 5, 2, 3, 6], 14029, [1, 1, 0, 15, 14, 13, 12, 10, 10, 9, 8, 7, 6, 4, 3, 5]),
  )
  @unpack
  def test_number_of_steps(self, init_memory, expected_steps, expected_init_cycle):
    memory_reallocator = MemoryReallocator(init_memory)
    init_cycle = memory_reallocator.count_number_steps()
    self.assertEquals(memory_reallocator.number_of_inserts, expected_steps)
    self.assertEquals(init_cycle, expected_init_cycle)

  @data(
    ([0, 2, 7, 0], 4),
    ([10, 3, 15, 10, 5, 15, 5, 15, 9, 2, 5, 8, 5, 2, 3, 6], 0),
  )
  @unpack
  def test_count_loop_size(self, init_memory, expected_loop_length):
    memory_reallocator = MemoryReallocator(init_memory)
    self.assertEquals(memory_reallocator.count_loop_size(), expected_loop_length)
