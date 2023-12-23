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

'''
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
# for x in bst:
#   print(x)

# print('len:',len(bst))
# print(bst) # preorder

print('find loc:',bst.find_loc(1)) # node(2)
print('search:',bst.search(1)) # None
print('insert:',bst.insert(1))
print('insert:',bst.insert(1))
print(bst)

#'''

'''
from my_BT import Node
from my_BST import BST

bst = BST()
bst.insert(2)
bst.insert(40)
bst.insert(20)
bst.insert(15)
bst.insert(5)
bst.insert(61)
bst.insert(32)
bst.insert(12)
print(bst)

#     2
#       \
#        40
#       /  \
#      20   61
#     /  \
#    15  32
#   /
#  5
#   \
#   12


# d=bst.deleteKeyByMerging(20)
# d=bst.deleteByMerging(20)
# print(d)
# print(bst)
# print(bst.root)
# print(bst.root.left)
# print(bst.maxNode(bst.root.left))
# print(bst.maxNode())
# print(bst.minNode())

d=bst.deleteNodeByCopying(bst.search(2))
# d=bst.deleteNodeByMerging(bst.search(15))
print(d)
print(bst)
# '''

# '''
from my_BT import Node
from my_BST import BST

bst = BST()
bst.insert(15)
bst.insert(4)
bst.insert(20)
bst.insert(17)
bst.insert(19)
bst.insert(32)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(8)
# bst.insert(2)
bst.insert(18)
bst.insert(16)
print(bst)

#      15
#     /   \
#    4     20
#   /     /  \
#  2    17    32
#       / \
#     16   19
#         / 
#       18 


# d=bst.deleteNodeByMerging(bst.search(20))
# d=bst.deleteNodeByCopying(bst.search(20))
d=bst.deleteByCopying(4)
# d=bst.deleteNodeByCopyingWithPrint(bst.search(4))
print(d)
print(bst)

# '''

'''
# from typing import override

class A:
  def __init__(self) -> None:
    pass
  # @override
  def funcStr(self,s:str):
    print('str:',s)
  # @override
  def funcInt(self,i:int):
    print('int:',i)
  
  def func(self, arg):
    if isinstance(arg, str):
      self.funcStr(arg)
    elif isinstance(arg, int):
      self.funcInt(arg)
    else:
      # 다른 타입에 대한 처리
      pass

a = A()
a.func('a')
a.func(1)
# '''

'''
import copy


class A:
  def __init__(self,val) -> None:
    self.val=val
  def __str__(self) -> str:
    return str(self.val)
  
a=A(10)
b=copy.copy(a)
print('a:',a) # 10
print('b:',b) # 10
b.val = 20
print('a:',a) # 10
print('b:',b) # 20
# '''