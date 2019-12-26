class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node
    
  def set_link_node(self, link_node):
    self.link_node = link_node
    
  def get_link_node(self):
    return self.link_node
  
  def get_value(self):
    return self.value

#Node example: Three nodes
yacko = Node("likes to yak")
wacko = Node("has a penchant for hoarding snacks")
dot = Node("enjoys spending time in movie lots")

#Link: yacko -> dot -> wacko
yacko.set_link_node(dot)
dot.set_link_node(wacko)

#Getting dot's data from yacko
dots_data = yacko.get_link_node().get_value()
print(dots_data)

#Getting wacko's data from dot
wackos_data = dot.get_link_node().get_value()
print(wackos_data)

