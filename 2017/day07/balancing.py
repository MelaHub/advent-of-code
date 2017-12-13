import collections
import re


NODE_REGEX = r'(?P<name>[a-z]+) \((?P<weight>[0-9]+)\)( -> (?P<balancing>.*))?'


class Node():

  name = None
  weight = None
  balancing = None
  sum_above = None

  def __init__(self, name, weight, balancing):
    self.name = name
    self.weight = weight
    self.balancing = balancing
    self.sum_above = 0


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

  def _find_unbalanced_node_res(self, node):
    if len(node.balancing) == 0:
      return (True, node)
    else:
      above_weights = []
      for above in node.balancing:
        is_balanced, above_node = self._find_unbalanced_node_res(self.nodes[above])
        if is_balanced is False:
          return (False, above_node)
        above_weights.append(above_node.sum_above + above_node.weight)
      node.sum_above = sum(above_weights)
      if len(set(above_weights)) == 1:
        return (True, node)
      else:
        return (False, node)

  def find_unbalanced_node(self):
    return [self._find_unbalanced_node_res(self.nodes[root]) for root in self.roots]

  def find_weight_to_balance_tree(self):
    for is_balanced, node in self.find_unbalanced_node():
      above_nodes = [self.nodes[node] for node in node.balancing]
      if len(above_nodes) < 3:
        raise Exception('Cannot find unbalanced node')
      balanced_weight = None
      wrong_node = None
      first_weight = above_nodes[0].weight + above_nodes[0].sum_above
      second_weight = above_nodes[1].weight + above_nodes[1].sum_above
      if first_weight == second_weight:
        balanced_weight = first_weight
      for node in above_nodes[2:]:
        node_weight = node.weight + node.sum_above
        if balanced_weight is None:
          if node_weight == first_weight: 
            balanced_weight = first_weight
            wrong_node = above_nodes[1]
          elif node_weight == second_weight:
            balanced_weight = second_weight
            wrong_node = above_nodes[0]
        if wrong_node is not None:
          break
        if node_weight != balanced_weight:
          wrong_node = node
    return wrong_node.weight - (wrong_node.weight + wrong_node.sum_above - balanced_weight)


def read_balance_from_file():
  balance_programs = BalancePrograms()
  with open('balancing') as f:
    for row in f.readlines():
      balance_programs.insert(row.strip())
  return balance_programs

def find_weight_to_balance_from_file():
  balance_tree = read_balance_from_file()
  return balance_tree.find_weight_to_balance_tree()
  

