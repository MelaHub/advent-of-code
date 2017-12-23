import collections
import re


NODE_REGEX = r'(?P<source>[0-9]+) <-> (?P<links>.+)'


class Pipes():

  graph = {}

  def _parse_input(self, input_links):
    match = re.search(NODE_REGEX, input_links)
    if len(match.groups()) < 2:
      raise Exception('Input is not formatted in the proper way')
    source = int(match.group('source'))
    links = [int(n) for n in match.group('links').replace(' ', '').split(',')]
    return source, links

  def add_link(self, link):
    source, links = self._parse_input(link)
    self.graph[source] = links

  def search_connected(self, source):
    visited_nodes = set()
    to_visit_nodes = [source]
    while len(to_visit_nodes):
      curr_node = to_visit_nodes.pop()
      visited_nodes.add(curr_node)
      to_visit_nodes += [node for node in self.graph.get(curr_node, []) if not node in visited_nodes]
    return visited_nodes

  def find_groups(self):
    groups = []
    to_check_nodes = self.graph.keys()
    while len(to_check_nodes):
      node = to_check_nodes[0]
      group = self.search_connected(node)
      to_check_nodes = [n for n in to_check_nodes if n not in group]
      groups.append(group)
    return groups
  
def _pipes_from_file(): 
  pipes = Pipes()
  with open('plumber') as f:
    for row in f.readlines():
      pipes.add_link(row.strip())
  return pipes

def search_from_file(source_node):
  pipes = _pipes_from_file()
  return pipes.search_connected(source_node)

def search_groups_from_file():
  pipes = _pipes_from_file()
  return pipes.find_groups()
