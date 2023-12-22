from my_BT import Node

class BST:
  def __init__(self,root:Node=None) -> None:
    self.root:Node = root
    self.size = 0 if root is None else len(root)
  def __len__(self):
    return self.size
  def __str__(self) -> str:
    return str(self.root.preorder())
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
  def find_loc(self,key)->Node|None:
    """key값 Node가 있다면 return 해당 Node / 없다면 Node가 insert될 return parent Node 

    Args:
        key (any): 위치를 확인하고 싶은 key

    Returns:
        Node|None: self Node or parent Node
    """
    if self.size == 0 or key is None:
      return None
    p = None
    v = self.root 
    while v is not None:
      if v.key == key: return v
      elif v.key < key:
        p = v
        v = v.right
      else:
        p = v
        v = v.left
    # not (key ∈ T) : return parent node 
    return p # parent node
  def search(self,key):
    v = self.find_loc(key)
    if v is None or v.key != key:
      return None
    return v