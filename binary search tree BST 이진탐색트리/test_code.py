# '''
from my_BT import Node

a6=Node(6)
b9=Node(9)
c1=Node(1)
d5=Node(5)

a6.left = b9
a6.right = c1
b9.parent = a6
c1.parent = a6
# b9.left = None
b9.right = d5
d5.parent = b9

#    6
#   / \
#  9   1
#   \
#    5

#'''