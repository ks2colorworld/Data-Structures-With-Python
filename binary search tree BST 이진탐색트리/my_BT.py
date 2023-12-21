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
  def preorder(self):
    str = ''
    if self is not None:
      # preorder()
      str = str + self.key + ','
      # print(self.key)
      if self.left is not None:
        str = str + self.left.preorder()
      # inorder()
      # str = str + self.key + ','
      # print(self.key)
      if self.right is not None:
        str = str + self.right.preorder()
      # postorder()
      # str = str + self.key + ','
      # print(self.key)
    return str 