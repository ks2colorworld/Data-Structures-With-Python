from my_node import MyNode

class MySinglyLinkedList:
  def __init__(self):
    self.size = 0
    self.head = None
    self.current = None
  def pushFront(self,key=None,value=None): # BigO(1)
    if key == None:
      self.size = 0
      self.head = None
      return 
    new_node = MyNode(key,value)
    new_node.next = self.head
    self.head = new_node
    self.size += 1
  def pushBack(self, key=None,value=None): # BigO(n)
    if key == None:
      return
    new_node = MyNode(key,value) # new_node.next = None
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
  def search(self, key):
    v = self.head
    while v != None:
      if v.key == key:
        break
      v = v.next
    return v # None
  def delete(self,key):
    if len(self) == 0:
      return None
    prev = None
    v = self.head
    while v != None:
      if v.key == key:
        if prev is not None:
          prev.next = v.next
        else:
          self.head = v.next
        self.size -= 1
        break
      prev = v
      v = v.next
    return v # x.key
  def __iter__(self): # for x in L: print(x) 
    self.current = self.head
    return self
  def __next__(self):
    if self.current is not None:
      x = self.current
      self.current = x.next
      # yield x # def __iterator__(self): 강의에서의 예시와 파이썬 문법이 상당히 다름.
      return x
    else:
      raise StopIteration
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