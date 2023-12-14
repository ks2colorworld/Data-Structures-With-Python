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
    self.__current = None # private 변수로 변경
  def __iter__(self):
    self.__current = self.head.next # head is dummy (None)
    return self
  def __next__(self):
    if self.__current.key != None:
      x = self.__current
      self.__current = x.next
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
    
  def search(self,key)->Node:
    i=None
    # ''' 구현된 __iter__ 문법 활용
    for a in self:
      if a.key == key:
        i = a 
        break
    # '''
    ''' 강의 내용 기준
    v = self.head
    while v.next != self.head:
      if v.key == key:
        i = v
        break
      v = v.next
    # '''
    return i 
  def remove(self,x:Node)->None:
    if x == None or x == self.head:
      return
    x.prev.next = x.next
    x.next.prev = x.prev
    self.size -= 1
  def popFront(self)->Node:
    if len(self) == 0:
      return None
    v = self.head.next
    self.remove(v) # self.size -= 1
    return v
  def popBack(self)->Node:
    if len(self) == 0:
      return None
    v = self.head.prev
    self.remove(v) # self.size -= 1
    return v
  def join(self,x:'DoublyLinkedList')->'DoublyLinkedList':
    if x == None or len(x) == 0:
      return self
    selfTail = self.head.prev
    xFront = x.head.next
    xTail = x.head.prev
    
    self.head.prev = xTail
    xTail.next = self.head
    selfTail.next = xFront
    xFront.prev = selfTail
    self.size += x.size
  def split(self,a:Node)->'DoublyLinkedList':
    """a 노드부터 tail 노드까지 잘라내서 새로운 양방향연결리스트로 반환한다.

    Args:
        a (Node): 잘라낼 리스트의 맨 첫번째 노드 

    Returns:
        DoublyLinkedList: 잘라낸 양방향연결리스트
    """
    X = DoublyLinkedList()
    if a == None:
      return X
    
    selfTail = a.prev
    XTail = self.head.prev
    
    a.prev = X.head
    X.head.next = a 
    
    X.head.prev = XTail
    XTail.next = X.head
    
    self.head.prev = selfTail
    selfTail.next = self.head
    
    for _ in X:
      X.size += 1
    self.size -= X.size
    return X