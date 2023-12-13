from my_node import MyNode

class MySinglyLinkedList:
  def __init__(self):
    self.size = 0
    self.head = None
  def pushFront(self,key=None): # BigO(1)
    if key == None:
      self.size = 0
      self.head = None
      return 
    new_node = MyNode(key)
    new_node.next = self.head
    self.head = new_node
    self.size += 1
  def pushBack(self, key=None): # BigO(n)
    if key == None:
      return
    new_node = MyNode(key) # new_node.next = None
    if len(self) == 0:
      self.size = 1
      self.head = new_node
      return
    tail = self.head # None? 
    while tail.next != None:
      tail = tail.next
    tail.nextNode(new_node)
    self.size += 1
  def popFront(self): # Big O(1)
    if len(self) == 0:
      return None
    x = self.head
    self.head = x.next
    self.size -= 1
    # key = x.key
    x.next = None # x.next의 링크를 끊음
    # del x # x(x.key)가 전달되지 않음
    return x # x.key
  def popBack2(self): # 직접 작성
    if len(self) == 0:
      return None
    if len(self) == 1:
      tail = self.head
      self.head = None
      self.size = 0
      return tail
    prev = self.head
    tail = prev.next
    while tail.next != None:
      prev = tail
      tail = prev.next
    prev.next = None
    self.size -= 1
    return tail
  def popBack(self): # 강의 기준 # BigO(n)
    if len(self) == 0:
      return None
    prev,tail = None,self.head
    while tail.next != None:
      prev = tail
      tail = prev.next
    if len(self) == 1:
      self.head = None
    else:
      prev.next = tail.next # None
    # del tail
    self.size -= 1
    return tail
  def __len__(self):
    return self.size
  def __str__(self):
    print(f'head:{self.head}, size:{self.size}')
    if len(self) == 0:
      return 'None->@'
    p = ''
    tail = self.head
    while tail.next != None:
      p=f'{p}{tail}->' # self.head->
      tail = tail.next
    return f'{p}{tail}->@'
  
  '''
  def pushFront(self,node=None):
    pass
  def insertNode(self, node=None):
    pass
  def deleteNode(self, node):
    pass
  def headNode(self,node=None):
    if node == None:
      self.size = 0 
      self.head = node
    if not isinstance(node, MyNode):
      raise ValueError("Input must be an instance of MyNode")
    if node.next == None:
      self.size = 1  
    self.head = node
  def setSize(self, sizeVal):
    self.size = sizeVal
  '''