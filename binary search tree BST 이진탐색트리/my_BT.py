class Node:
  def __init__(self,key,*,parent:'Node'=None,left:'Node'=None,right:'Node'=None,) -> None:
    self.key = key
    self.parent = parent
    self.left = left
    if left is not None:
      self.left.parent = self
    self.right = right
    if right is not None:
      self.right.parent = self
  def __str__(self) -> str:
    return str(self.key)