from my_BT import Node

class BST:
  def __init__(self) -> None:
    self.root:Node = None
    self.size = 0
    #
    # (for test)
    # self.root:Node = Node(15,\
    #   left=Node(4,  left=Node(2)),\
    #   right=Node(20,left=Node(17,\
    #                             right=Node(19)),\
    #                 right=Node(32)))
    # self.size = 7
    #
  def __iter__(self):
    if self.root is None:
      return iter([])  # Return an empty iterator if there is no root node.
      # raise IndexError('no root node!')
    if not isinstance(self.root,Node):
      raise IndexError('root is not Node!')
    return self.root.__iter__() # preorder()
  def __next__(self):
    if self.root is None:
      raise StopIteration
      # raise IndexError('no root node!')
    return self.root.__next__()