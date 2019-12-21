class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node


  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None
    self.length = 0

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node
    self.length += 1


  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def print_self(self):
    print("debug")
    node = self.head
    while node is not None:
      print(node.get_value())
      node = node.get_next()

  def reverse_list(self):
    if self.length == 0 or self.length == 1:
      return

  # break the list
    old_head = self.head
    old_head_next = self.head.get_next()

    old_head.set_next(None)
    self.length = 1
    node = old_head_next
    while node is not None:
      _node = node.get_next()
      # print('node',node.get_value())
      self.add_to_head(node.get_value())
      node = _node
      # if node:
        # print('node',node.get_value())
      # self.print_self()


    # # find the node to insert, start with tail
    # node_to_move = self.head
    # for _ in range(self.length-1):
    #   node_to_move = node_to_move.get_next()
    # node_to_insert = node_to_move
    # print("node_to_insert", node_to_insert.get_value())
    #
    # # move nodes
    # for _ in range(self.length):
    #   node_to_move = self.head
    #   self.head = self.head.get_next() # save the head
    #   print("node_to_move", node_to_move.get_value())
    #   print("node_to_insert", node_to_insert.get_value())
    #   node_to_insert.set_next(node_to_move)
    #   node_to_insert = node_to_move
    #   node_to_move.set_next(None)
    #   # node_to_move = node_to_move.get_next()

      #debug



