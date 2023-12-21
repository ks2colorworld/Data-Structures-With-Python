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
  def preorder(self)->list:
    A = []
    if self is not None:
      # preorder()
      A.append(self.key)
      # print(self.key)
      if self.left is not None:
        A.extend(self.left.preorder())
      # inorder()
      # print(self.key)
      if self.right is not None:
        A.extend(self.right.preorder())
      # postorder()
      # print(self.key)
    return A 
  def inorder(self)->list:
    A = []
    if self is not None:
      # preorder()
      # print(self.key)
      if self.left is not None:
        A.extend(self.left.inorder())
      # inorder()
      A.append(self.key)
      # print(self.key)
      if self.right is not None:
        A.extend(self.right.inorder())
      # postorder()
      # print(self.key)
    return A 