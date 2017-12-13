import re


NODE_REGEX = r'(?P<name>[a-z]+) \((?P<weight>[0-9]+)\)( -> (?P<balancing>.*))?'


class Node():

  name = None
  weight = None
  balancing = None

  def __init__(self, name, weight, balancing):
    self.name = name
    self.weight = weight
    self.balancing = balancing


class BalancePrograms():

  roots = None
  nodes = None
  all_nodes_names = None

  def __init__(self):
    self.roots = set()
    self.nodes = {}
    self.all_nodes_names = set()

  def _parse_program(self, input_string):
    match = re.search(NODE_REGEX, input_string)
    if len(match.groups()) < 2:
      raise Exception('Input is not formatted in the proper way')
    name = match.group('name')
    weight = int(match.group('weight'))
    balancing = match.group('balancing')
    if balancing is None:
      balancing = []
    else:
      balancing = balancing.replace(' ', '').split(',')
    return name, weight, balancing

  def insert(self, input_string):
    name, weight, balancing = self._parse_program(input_string)
    new_node = Node(name, weight, balancing)
    self.nodes[new_node.name] = new_node
    for node in new_node.balancing:
      self.all_nodes_names.add(node)
      if node in self.roots:
        self.roots.remove(node)
    if new_node.name not in self.all_nodes_names:
      self.roots.add(new_node.name) 


def find_root_from_file():
  balance_programs = BalancePrograms()
  with open('balancing') as f:
    for row in f.readlines():
      balance_programs.insert(row.strip())
  return balance_programs.roots
    
