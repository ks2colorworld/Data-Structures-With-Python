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
    self.__preorderList=[]
    self.__current=-1
  def __str__(self) -> str:
    return str(self.key)
  def __iter__(self):
    self.__preorderList = self.preorder()
    if 0<len(self.__preorderList):
      self.__current = 0 # self.__preorderList[0]
    else:
      self.__current = -1
    return self
  def __next__(self):
    if 0<=self.__current: # -1
      x = self.__current
      self.__current = x + 1
      if x == len(self.__preorderList):
        raise StopIteration
      return self.__preorderList[x]
    else:
      raise StopIteration
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