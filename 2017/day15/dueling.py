class Generator(object):
  
  curr_value = None
  factor = None
  remainder_of = 2147483647

  def __init__(self, starting_value, factor):
    self.curr_value = starting_value
    self.factor = factor

  def gen_next(self):
    return NotImplementedError()

class GeneratorFirstHalf(Generator):

  def gen_next(self):
    while True:
      self.curr_value = (self.curr_value * self.factor) % self.remainder_of
      yield self.curr_value
  
class GeneratorAFirstHalf(GeneratorFirstHalf):
  def __init__(self, starting_value):
    factor = 16807
    super(GeneratorAFirstHalf, self).__init__(starting_value, factor)

class GeneratorBFirstHalf(GeneratorFirstHalf):
  def __init__(self, starting_value):
    factor = 48271
    super(GeneratorBFirstHalf, self).__init__(starting_value, factor)

class GeneratorSecondHalf(Generator):

  divisor = None

  def __init__(self, starting_value, factor, divisor):
    self.divisor = divisor
    super(GeneratorSecondHalf, self).__init__(starting_value, factor)

  def gen_next(self):
    while True:
      self.curr_value = (self.curr_value * self.factor) % self.remainder_of
      if (self.curr_value % self.divisor) == 0:
        yield self.curr_value
    

class GeneratorASecondHalf(GeneratorSecondHalf):
  def __init__(self, starting_value):
    factor = 16807
    divisor = 4
    super(GeneratorASecondHalf, self).__init__(starting_value, factor, divisor)

class GeneratorBSecondHalf(GeneratorSecondHalf):
  def __init__(self, starting_value):
    factor = 48271
    divisor = 8
    super(GeneratorBSecondHalf, self).__init__(starting_value, factor, divisor)


class Judge(object):

  generators = []

  def __init__(self, list_generators):
    self.generators = list_generators

  def are_statuses_equal(self, values):
    return len(set([v & 0xFFFF for v in values])) == 1

  def judge(self, n_rounds):
    correct_rounds = 0
    generators = [gen.gen_next() for gen in self.generators]
    for i in range(n_rounds):
      if self.are_statuses_equal([gen.next() for gen in generators]):
        correct_rounds += 1
    return correct_rounds
    
