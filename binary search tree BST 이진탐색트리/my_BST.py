import copy
from my_BT import Node

class BST:
  def __init__(self,root:Node=None) -> None:
    self.root:Node = root
    self.size = 0 if root is None else len(root)
  def __len__(self):
    return self.size
  def __str__(self) -> str:
    return str(self.root.inorder()) # preorder()
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
    # key ∉ BST (key가 BST에 포함되어 있지 않다) : return parent node 
    return p # parent node
  def search(self,key):
    v = self.find_loc(key)
    if v is None or v.key != key:
      return None
    return v
  def insert(self,key):
    p = self.find_loc(key)
    if p is None or p.key is not key:
      v = Node(key)
      if p is None:
        self.root = v
      else: # p is not None and p.key is not key
        v.parent = p
        if key <= p.key:
          p.left = v
        else:
          p.right = v
      self.size += 1
      return v
    else: print(f"key '{key}' has already been inserted")
    return None
  def deleteByMerging(self,key_or_node:Node|int)->Node|int|None:
    if isinstance(key_or_node, Node):
      return self.deleteNodeByMerging(key_or_node)
    elif isinstance(key_or_node, int):
      return self.deleteKeyByMerging(key_or_node)
    else:
      return None
  def deleteNodeByMerging(self,x:Node)->Node|None:
    if x is None:
      return None
    # 1. a(x.left) is None
    # 2. x is root node (x.parent is None)
    a=x.left
    b=x.right
    pt=x.parent
    c=None # x자리를 대체할 노드
    m=None # L(a가 root인 트리)에서 가장 큰 노드
    if a is not None:
      c=a
      m=a
      while m.right is not None:
        m=m.right
      m.right=b
      if b is not None:
        b.parent=m
    else: # 1. a is None
      c=b 
    # next step
    if pt is not None:
      if c is not None: c.parent = pt
      if pt.key < c.key:
        pt.right = c
      else:
        pt.left = c
    else: # 2. x is root node
      self.root = c
      if c is not None: c.parent = None
    self.size -= 1
    return x
  def deleteKeyByMerging(self,key:int)->int|None:
    v=self.find_loc(key)
    if v is not None and v.key is key:
      x = self.deleteNodeByMerging(v)
      return x.key
    else:
      return None
  
  def deleteByCopying(self,key_or_node:Node|int)->Node|int|None:
    if isinstance(key_or_node, Node):
      return self.deleteNodeByCopying(key_or_node)
    elif isinstance(key_or_node, int):
      return self.deleteKeyByCopying(key_or_node)
    else:
      return None
  def deleteKeyByCopying(self,key:int)->int|None:
    v=self.find_loc(key)
    if v is not None and v.key is key:
      x = self.deleteNodeByCopying(v)
      return x.key
    else:
      return None
  def deleteNodeByCopying(self,x:Node):
    if x is None:
      return None
    #      15
    #     /   \
    #    4     20
    #   /     /  \
    #  2    17    32
    #       / \
    #     16   19
    #         / 
    #       18 
    
    # ''' 2
    a=x.left
    b=x.right
    pt=x.parent
    c=None
    m=self.maxNode(a) 
    if a is not None and m is not None: 
      c=copy.copy(m)
    else: 
      c=b
    if c is not None:
      c.parent,c.left,c.right = x.parent,x.left,x.right
    else: # c is None
      if pt.left is x:
        pt.left = None
      else: #pt.right
        pt.right = None
      return x
    
    if c.left is not None:
      c.left.parent = c
      if c.left is not m:
        m.parent.right = m.left
      else:
        c.left = c.left.left
      if m.left is not None:
        m.left.parent = m.parent
    
    if c.right is not None:
      c.right.parent = c
    
    if pt is None:
      self.root = c
    else:
      if pt.key < x.key:
        pt.right = c
      else:
        pt.left = c
    # '''
    self.size -= 1
    return x

  def maxNode(self,x:Node=None):
    if x is None:
      x = self.root
    if x is None:
      return None
    if x.left is None and x.right is None:
      return x
    m = x.right
    while m is not None and m.right is not None:
      m = m.right
    return x if m is None else m
  def minNode(self,x:Node=None):
    if x is None:
      x = self.root
    if x is None:
      return None
    if x.left is None and x.right is None:
      return x
    m = x.left
    while m is not None and m.left is not None:
      m = m.left
    return x if m is None else m

  def deleteNodeByCopyingWithPrint(self,x:Node):
    print('x:',self.printNode(x))
    if x is None:
      return None
    #      15
    #     /   \
    #    4     20
    #   /     /  \
    #  2    17    32
    #       / \
    #     16   19
    #         / 
    #       18 
    
    # ''' 2
    a=x.left
    print('a:',self.printNode(a))
    b=x.right
    print('b:',self.printNode(b))
    pt=x.parent
    print('pt:',self.printNode(pt))
    c=None
    print('c:',self.printNode(c))
    m=self.maxNode(a) 
    print('m:',self.printNode(m))
    print('--1--')
    if a is not None and m is not None: 
      c=copy.copy(m)
    else: 
      c=b
    print('c:',self.printNode(c))
    if c is not None:
      c.parent,c.left,c.right = x.parent,x.left,x.right
    else: # c is None
      if pt.left is x:
        pt.left = None
      else: #pt.right
        pt.right = None
      return x
      
    print('--2--')
    print('c:',self.printNode(c))
    print('c.left:',self.printNode(c.left))
    print('c.right:',self.printNode(c.right))
    print('m:',self.printNode(m))
    
    if c.left is not None:
      print('c.left.parent:',self.printNode(c.left.parent))
      c.left.parent = c
      print('c.left.parent:',self.printNode(c.left.parent))
      print('m:',self.printNode(m))
      if c.left is not m:
        m.parent.right = m.left
      else:
        c.left = c.left.left
      if m.left is not None:
        m.left.parent = m.parent
        
    print('--3--')
    print('c:',self.printNode(c))
    print('c.left:',self.printNode(c.left))
    print('c.right:',self.printNode(c.right))
    print('m:',self.printNode(m))
    
    if c.right is not None:
      c.right.parent = c
      
    print('--4--')
    print('c:',self.printNode(c))
    print('c.left:',self.printNode(c.left))
    print('c.right:',self.printNode(c.right))
    
    if pt is None:
      self.root = c
    else:
      if pt.key < x.key:
        pt.right = c
      else:
        pt.left = c
        
    print('--5--')
    print('pt:',self.printNode(pt))
    print('c:',self.printNode(c))
    print('c.left:',self.printNode(c.left))
    print('c.right:',self.printNode(c.right))
    # '''
    
    ''' 1 first
    a=x.left
    b=x.right
    pt=x.parent
    if a is None and b is None: # x is leaf node or one root node  # x = 2,16,32
      if pt is None: # x = (root)
        self.root = None
        return None
      if pt.key < x.key: # x = 32
        pt.right = None
      else: # x = 2,16
        pt.left = None
      return x
    
    c = None # x자리를 대체할 노드
    m = self.maxNode(a) # L(a가 root인 트리)에서 가장 큰 노드
    if a is not None:
      c = m # or a 
    else: # a is None and b is not None 
      c = b # b is not None
      
    if pt is None: # x is root node
      self.root = c
    else:
      if pt.key < x.key: # x = 20, 32, 19
        pt.right = c
      else: 
        pt.left = c
    
    if c is not a:
      if m.left is not None:
        m.parent.right, m.left.parent = m.left, m.parent
      c.left,a.parent = a,c
    if c is not b:
      c.right = b 
      if b is not None:
        b.parent = c
    #'''
    
    self.size -= 1
    return x
  def printNode(self,x:Node):
    if x is None:
      return 'None'
    return 'node(k:'+str(x.key)+',p:'+str(x.parent)+',l:'+str(x.left)+',r:'+str(x.right)+')'