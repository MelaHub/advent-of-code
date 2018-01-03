class Link(object):

  from_link = None
  to_link = None
  link_types = None
  strength = None

  def __init__(self, input_string):
    self.link_types = [int(i) for i in input_string.split('/')]
    self.strength = sum(self.link_types) 
  
