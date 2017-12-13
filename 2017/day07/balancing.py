# classe node
# classe tree
  # parser di un input
  # insert -> cerca il nodo e sistema il tree
  # tree rappresentato come una hashmap
import re


NODE_REGEX = r'(?P<name>[a-z]+) \((?P<weight>[0-9]+)\)( -> (?P<balancing>.*))?'


class BalancePrograms():

  roots = None

  def __init__(self):
    self.roots = {}

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
    
