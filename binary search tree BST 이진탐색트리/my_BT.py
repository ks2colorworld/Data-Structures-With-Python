class Node:
  def __init__(self,key=int) -> None:
    self.key = key
    self.parent = self.left = self.right = None
  def __str__(self) -> str:
    return str(self.key)