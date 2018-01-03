class Link(object):

  link_id = None
  from_link = None
  to_link = None
  link_types = None
  strength = None

  def __init__(self, link_id, input_string):
    self.link_id = link_id
    self.link_types = [int(i) for i in input_string.split('/')]
    self.strength = sum(self.link_types)

  def set_from_link(self, from_node):
    self.from_link = from_node
    self.to_link = self.link_types[0]
    if self.link_types[0] == from_node:
      self.to_link = self.link_types[1]

  def contains(self, node):
    return node in self.link_types

  def __eq__(self, other):
    return self.link_id == other.link_id

  def __str__(self):
    return '/'.join([str(i) for i in self.link_types])


def links_from_string(links):
  return [Link(i, link) for i, link in enumerate(links)]


def build_bridges_rec(current_link, remaining_links):
  if len(remaining_links) == 0:
    return [[current_link]]
  current_link_links = [[current_link]]
  for link in remaining_links:
    if link.contains(current_link.to_link):
      new_link = Link(link.link_id, '%s' % link)
      new_link.set_from_link(current_link.to_link)
      current_links = build_bridges_rec(new_link, [l for l in remaining_links if l != link])
      current_link_links += [[current_link] + bridge for bridge in current_links]
  return current_link_links


def build_bridges(links):
  origin_node = Link(-1, '0/0')
  origin_node.set_from_link(0)
  return [
    bridge[1:]
    for bridge in build_bridges_rec(origin_node, links)    
    if len(bridge[1:]) > 0
  ]

def max_strength(links):
  bridges = build_bridges(links)
  return max([sum([link.strength for link in bridge]) for bridge in bridges])
