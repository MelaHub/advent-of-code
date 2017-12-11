import operator

class MemoryReallocator(object):

  memory = None
  starting_memory = None

  def __init__(self, init_memory):
    self.memory = {}
    self._insert_in_memory(init_memory)
    self.starting_memory = init_memory

  def _insert_in_memory(self, blocks):
    subtree = self.memory
    for block in blocks:
      subtree.setdefault(block, {})
      subtree = subtree.get(block)

  def _one_step(self, memory):
    new_memory = [block for block in memory]
    max_index, max_value = max(enumerate(new_memory), key=operator.itemgetter(1))
    new_memory[max_index] = 0
    for i in range(0, max_value):
      max_index += 1
      if max_index >= len(new_memory):
        max_index = 0
      new_memory[max_index] += 1
    return new_memory

  def _find_in_memory_rec(self, blocks, memory_search):
    if len(blocks) == 0 and len(memory_search.keys()) == 0:
      return True
    if len(blocks) == 0 or len(memory_search.keys()) == 0:
      return False
    submemory = memory_search.get(blocks[0])
    if submemory is None:
      return False
    else:
      return self._find_in_memory_rec(blocks[1:], submemory)

  def _find_in_memory(self, blocks):
    return self._find_in_memory_rec(blocks, self.memory)

  # rec version encounter max num of recursions reached error
  def _count_number_steps_rec(self, curr_iteration, curr_memory):
    if self._find_in_memory(curr_memory):
      return curr_iteration
    self._insert_in_memory(curr_memory)
    next_memory = self._one_step(curr_memory)
    return self._count_number_steps_rec(curr_iteration + 1, next_memory)

  def _count_number_steps_non_rec(self):
    curr_memory = self._one_step(self.starting_memory)
    curr_number_of_steps = 1
    while not self._find_in_memory(curr_memory):
      self._insert_in_memory(curr_memory)
      curr_memory = self._one_step(curr_memory)
      curr_number_of_steps += 1
    return curr_number_of_steps

  def count_number_steps(self):
    return self._count_number_steps_non_rec()
    # reallocate = self._one_step(self.starting_memory)
    # return self._count_number_steps_rec(1, reallocate)
    
