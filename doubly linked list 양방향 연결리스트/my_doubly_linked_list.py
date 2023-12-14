# Circularly Doubly Linked List Node

class Node: 
  def __init__(self, key=None) -> None: # type hinting ('-> None'): 코드 실행에는 영향을 미치지 않음
    self.key = key
    self.next = self
    self.prev = self
  def __str__(self):
    selfString = f'node[{str(self.key)}]'
    return f'{selfString}'

class DoublyLinkedList: 
  def __init__(self) -> None:
    self.head = Node() # head node 혹은 dummy node 
    self.size = 0
    self.current = None
  def __iter__(self):
    self.current = self.head.next # head is dummy (None)
    return self
  def __next__(self):
    if self.current.key != None:
      x = self.current
      self.current = x.next
      return x
    else:
      raise StopIteration
  def __str__(self) -> str:
    print(f'head:{self.head}, size:{self.size}')
    if len(self) == 0:
      return '(tailNode)<-DummyNode->(headNode)'
    p = '(tailNode)<-DummyNode<->'
    tail = self.head.next
    while tail.next.key != None:
      p = f'{p}{tail}<->'
      tail = tail.next
    return f'{p}{tail}->(headNode)'
  def __len__(self):
    return self.size