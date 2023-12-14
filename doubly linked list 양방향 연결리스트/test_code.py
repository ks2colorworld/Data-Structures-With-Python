from my_doubly_linked_list import Node, DoublyLinkedList

L = DoublyLinkedList()
print(L)
'''
head:node[None], size:0
(tailNode)<-DummyNode->(headNode)
'''

h = Node()
a = Node(1)
h.next = a
h.prev = a
a.next = h
a.prev = h
b = Node(2)
# ''' h에 b가 있(없)는 조건
b.next = h
b.prev = a 
a.next = b 
h.prev = b
# '''
x = Node(3)
''' x가 a 다음에 있(없)는 조건
a.next = x
x.prev = a 
x.next = b 
b.prev = x 
# '''
''' x가 다른 h2 리스트에 있는 조건 
h2 = Node()
h2.next = x
h2.prev = x
x.next = h2
x.prev = h2
# '''

# L.splice(a,b,x)


L.pushFront(3)
# L.pushBack(-1)
n_1 = Node(-1)
# L.insertBefore(L.head,n_1)
L.pushNodeBack(n_1)
L.pushBack(9)

n5 = Node(5)
L.insertAfter(n_1,n5)

print(L)
'''
head:node[None], size:4
(tailNode)<-DummyNode<->node[3]<->node[-1]<->node[5]<->node[9]->(headNode)
#'''