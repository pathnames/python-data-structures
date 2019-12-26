# Linked List requires a slight modification to node:
class Node:
  def __init__(self, value, next_node = None):
    self.value = value
    self.next_node = next_node
  
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node
    
#Example:
my_node = Node(44)
print(my_node.get_value)
  
#Linked List class
#Methods supported: 
#1) get_head_node(): Returns the head node of the linked list
#2) insert_beginning(new_value): Inserts a new node at the beginning of the linked list with the value = new_value
#3) stringify_list(): Returns the linked list as a string, with each node's value seperated on a new line
#4) add_node(previous_value, new_value): Inserts a new node (with value = new_value) after the first occurrence of a node with the value = previous_value
#5) remove_node(value_to_remove): Removes the node with value = value_to_remove from the linked list
 

class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list

  def add_node(self, previous_value, new_value):
      current_node = self.head_node
      while current_node:
          if current_node.get_value() == previous_value:
              new_node = Node(new_value)
              new_node.set_next_node = current_node.get_next_node()
              current_node.set_next_node(new_node)
              current_node = None
          else:
              current_node = current_node.get_next_node()
  
  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node
  
  
#Example
ll = LinkedList(1)
ll.add_node(1, 2)
print(ll.stringify_list())

#Output: 
#1
#2 

ll.remove_node(1)
print(ll.stringify_list())
#Output:
#2