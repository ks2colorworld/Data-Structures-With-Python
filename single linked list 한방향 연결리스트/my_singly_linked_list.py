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