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
  
  def splice(self,a:Node,b:Node,x:Node):
    """a~b까지의 Node들을 잘라내서 x Node 다음에 붙여 넣습니다.
    조건1: a <-> ... <-> b (a 다음에 b가 나와야 한다)
    조건2: a와 b사이에 head node와 x가 없음
    
    Args:
        a (Node): 시작 Node
        b (Node): 마지막 Node
        x (Node): 붙여 넣을 Node 위치

    Raises:
        TypeError: All parameters must be an instance of Node.
    """
    if not isinstance(a, Node) or \
      not isinstance(b, Node) or \
      not isinstance(x, Node):
        raise TypeError("All parameters must be an instance of Node.")
    
    # 조건1: a <-> ... <-> b (a 다음에 b가 나와야 한다)
    # 조건2: a와 b사이에 head node와 x가 없음
    
    # ''' 
    # 조건 확인 로직 (강의 내용에는 없음)
    nextNode = a.next
    # if a == nextNode:
    #   raise ValueError('조건 1 : a 노드 뒤에 b 노드가 위치해야 한다')
    is_b_after_a = (a == nextNode) # nextNode.key != None
    while is_b_after_a is not True and nextNode.key != None:
      if nextNode == b: # 조건1 만족 : a <-> ... <-> b (a 다음에 b가 있음)
        is_b_after_a = True
        break
      if nextNode == x:
        is_b_after_a = False
        raise ValueError("조건 2 : a,b 사이에 x 노드가 없어야 한다")
        break
      nextNode = nextNode.next
      if nextNode.key == None: # 조건1,2 불만족 : a 다음에 b가 나타나기 전에 head node가 있음
        is_b_after_a = False 
        break
    if is_b_after_a is not True:
      raise ValueError("조건 2 : a,b 사이에 head 노드가 없어야 한다")
    # '''
    
    
    # 전 : ap(a.prev) <-> a <-> ... <-> b <-> bn(b.next)
    # 전 : x <-> xn(x.next)
    # 후 : ap <-> bn
    # 후 : x <-> a <-> ... <-> b <-> xn
    
    ap = a.prev
    bn = b.next
    xn = x.next
    
    ap.next = bn
    bn.prev = ap
    x.next = a 
    a.prev = x
    b.next = xn
    xn.prev = b
    
  def moveAfter(self,a:Node,x:Node):
    self.splice(a,a,x)
  def moveBefore(self,a:Node,x:Node):
    self.splice(a,a,x.prev)
    
  def insertAfter(self,x:Node,a:Node):
    self.moveAfter(a,x)
    self.size += 1
  def insertBefore(self,x:Node,a:Node):
    self.moveBefore(a,x)
    self.size += 1
    
  def pushFront(self,key):
    self.insertAfter(self.head,Node(key))
  def pushBack(self,key):
    self.insertBefore(self.head,Node(key))
  
  def pushNodeFront(self,a:Node):
    self.insertAfter(self.head,a)
  def pushNodeBack(self,a:Node):
    self.insertBefore(self.head,a)