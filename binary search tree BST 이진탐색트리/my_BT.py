class Node:
  def __init__(self,key,*,parent:'Node'=None,left:'Node'=None,right:'Node'=None,) -> None:
    self.key = key
    self.parent = parent
    self.left = left
    self.right = right
    self.height = 1 # for AVL BST
    # self.__preorderList=[]
    self.__inorderList=[]
    self.__current=-1
  def __str__(self) -> str:
    return str(self.key)
  def __iter__(self):
    # self.__preorderList = self.preorder()
    self.__inorderList = self.inorder()
    # if 0<len(self.__preorderList):
    if 0<len(self.__inorderList):
      self.__current = 0 # self.__preorderList[0]
    else:
      self.__current = -1
    return self
  def __next__(self):
    if 0<=self.__current: # -1
      x = self.__current
      self.__current = x + 1
      # if x == len(self.__preorderList):
      if x == len(self.__inorderList):
        raise StopIteration
      # return self.__preorderList[x]
      return self.__inorderList[x]
    else:
      raise StopIteration
  def __len__(self):
    # return len(self.preorder())
    return len(self.inorder())
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
  
  def printNode(self, withHeight:bool=False):
    x = self
    if withHeight:
      return 'node(k:'+str(x.key)+',p:'+str(x.parent)+',l:'+str(x.left)+',r:'+str(x.right)+',height:'+str(x.height)+')'
    else:
      return 'node(k:'+str(x.key)+',p:'+str(x.parent)+',l:'+str(x.left)+',r:'+str(x.right)+')'
  
  @property
  def parent(self):
    return self.__parent

  @parent.setter
  def parent(self, node:'Node'):
    self.__parent = node
    # if node is None:
    #   return
    # if self.__parent.key < self.key:
    #   self.__parent.right = self
    # else: self.__parent.left = self
  
  @property
  def left(self):
    return self.__left

  @left.setter
  def left(self, node:'Node'):
    self.__left = node
    if node is None:
      return
    self.__left.parent = self
  
  @property
  def right(self):
    return self.__right

  @right.setter
  def right(self, node:'Node'):
    self.__right = node
    if node is None:
      return
    self.__right.parent = self
  