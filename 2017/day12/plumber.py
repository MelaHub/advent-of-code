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
