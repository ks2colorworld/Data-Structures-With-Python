from my_node import MyNode
from my_singly_linked_list import MySinglyLinkedList

# [3] -> [9] -> [-1] -> @  
a = MyNode(3)
b = MyNode(9)
c = MyNode(-1)
a.nextNode(b)
b.nextNode(c)

print(a) # node[3]
print(b) # node[9]
print(c) # node[-1]

'''
L 
head [node(3)]
size [3]

node[3] -> node[9] -> node[-1] -> @ 
'''

L = MySinglyLinkedList()
# L.pushFront(MyNode(-1)) # node[-1] -> @ 
# L.pushFront(MyNode(9))  # node[9] -> node[-1] -> @ 
# L.pushFront(MyNode(3))  # node[3] -> node[9] -> node[-1] -> @ 

L.pushFront(-1) # node[-1] -> @ 
L.pushFront(9)  # node[9] -> node[-1] -> @ 
L.pushFront(3)  # node[3] -> node[9] -> node[-1] -> @ 
L.pushFront(5)  # node[5] -> node[3] -> node[9] -> node[-1] -> @ 
L.pushBack(4)   # node[5] -> node[3] -> node[9] -> node[-1] -> node[4] -> @

print(L)
'''
head:node[5], size:5
node[5]->node[3]->node[9]->node[-1]->node[4]->@
'''

print('seach(9) :', L.search(9)) # seach(9) : node[9]
print(L.popFront()) # node[5]
print(L.popBack()) # node[4]
# print(L.popBack()) 
# print(L.popBack()) 
# print(L.popFront())
# print(L.popBack()) 
# print(L.popBack()) 

print(L)

print('seach(5) :', L.search(5)) # seach(5) : None

for x in L : print(x)
'''
node[3]
node[9]
node[-1]
'''