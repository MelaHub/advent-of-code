import operator

class MemoryReallocator(object):

  memory = None
  starting_memory = None
  number_of_inserts = 0

  def __init__(self, init_memory):
    self.memory = {}
    self._insert_in_memory(init_memory)
    self.starting_memory = init_memory

  def _insert_in_memory(self, blocks):
    subtree = self.memory
    if not len(blocks):
      return
    for block in blocks[:-1]:
      subtree.setdefault(block, {})
      subtree = subtree.get(block)
    subtree.setdefault(blocks[-1], self.number_of_inserts)
    self.number_of_inserts += 1

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

  def _is_leaf(self, memory_search):
    return type(memory_search) == int

  def _find_in_memory_rec(self, blocks, memory_search):
    if len(blocks) == 0 and self._is_leaf(memory_search):
      return memory_search
    if len(blocks) == 0 or self._is_leaf(memory_search):
      return -1
    submemory = memory_search.get(blocks[0])
    if submemory is None:
      return -1
    else:
      return self._find_in_memory_rec(blocks[1:], submemory)

  def _find_in_memory(self, blocks):
    return self._find_in_memory_rec(blocks, self.memory)

  # rec version encounter max num of recursions reached error
  def _count_number_steps_rec(self, curr_iteration, curr_memory):
    if self._find_in_memory(curr_memory) > -1:
      return curr_iteration
    self._insert_in_memory(curr_memory)
    next_memory = self._one_step(curr_memory)
    return self._count_number_steps_rec(curr_iteration + 1, next_memory)

  def _count_number_steps_non_rec(self):
    curr_memory = self._one_step(self.starting_memory)
    while self._find_in_memory(curr_memory) == -1:
      self._insert_in_memory(curr_memory)
      curr_memory = self._one_step(curr_memory)
    return curr_memory

  def count_number_steps(self):
    return self._count_number_steps_non_rec()
    # reallocate = self._one_step(self.starting_memory)
    # return self._count_number_steps_rec(1, reallocate)
   
  def count_loop_size(self):
    curr_memory = self._count_number_steps_non_rec()
    number_of_insert_of_init_loop = self._find_in_memory(curr_memory)
    return self.number_of_inserts - number_of_insert_of_init_loop
