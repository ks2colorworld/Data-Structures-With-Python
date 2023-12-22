'''
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

'''
from my_BT import Node

root = Node(6,left=Node(9,right=Node(5)),right=Node(1))
#    6
#   / \
#  9   1
#   \
#    5

#'''

'''
from my_BT import Node

root = Node('F',\
  left=Node('B',left=Node('A'),\
                right=Node('D', left=Node('C'),\
                                right=Node('E'))),\
  right=Node('G',right=Node('I',left=Node('H'))))
  #       F
  #     /   \
  #    B      G
  #   / \      \
  #  A   D      I
  #     / \    /
  #    C   E  H 

# print(root.preorder()[:-1]) # 문자열[:-n] 뒤에서부터 n개의 문자열 지우는 문법
print(root.preorder()) # list
# print(root.inorder()) # list
for x in root:
  print(x) # preorder()
#'''

#'''
from my_BT import Node
from my_BST import BST

root = Node(15,\
      left=Node(4,  left=Node(2)),\
      right=Node(20,left=Node(17,\
                                right=Node(19)),\
                    right=Node(32)))
  #      15
  #     /   \
  #    4     20
  #   /     /  \
  #  2    17    32
  #         \
  #          19

bst = BST(root)
for x in bst:
  print(x)

print('len:',len(bst))
print(bst) # preorder
#'''
