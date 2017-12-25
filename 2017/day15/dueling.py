class Generator(object):
  
  curr_value = None
  factor = None
  remainder_of = 2147483647

  def __init__(self, starting_value, factor):
    self.curr_value = starting_value
    self.factor = factor

  def gen_next(self):
    self.curr_value = (self.curr_value * self.factor) % self.remainder_of
    return self.curr_value

class GeneratorA(Generator):
  def __init__(self, starting_value):
    factor = 16807
    super(GeneratorA, self).__init__(starting_value, factor)

class GeneratorB(Generator):
  def __init__(self, starting_value):
    factor = 48271
    super(GeneratorB, self).__init__(starting_value, factor)


class Judge(object):

  generators = []

  def __init__(self, list_generators):
    self.generators = list_generators

  def are_statuses_equal(self, values):
    return len(set([bin(v)[-16:] for v in values])) == 1
