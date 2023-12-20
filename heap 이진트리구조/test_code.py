'''
# 힙 성질을 만족하지 않는 리스트
A = [2,8,6,1,10,15,3,12,11]
# 리스트를 이진트리로 표시했을 때
#        2
#      /   \
#     8      6
#    / \    /  \
#   1  10  15   3
#  /  \
# 12  11

# 힙 성질을 만족하도록 수정된 리스트
A2 = [15,12,6,11,10,2,3,1,5]
#         15
#       /    \
#     12       6
#    /  \     /  \
#   11   10   2   3
#  / \
# 1   5
#'''

''' make-heap
from my_heap import Heap
#    0 1 2 3 4  5  6 7  8  len:9
A = [2,8,6,1,10,15,3,12,11]
# 리스트를 이진트리로 표시했을 때
#        2
#      /   \
#     8      6
#    / \    /  \
#   1  10  15   3
#  /  \
# 12  11

hp = Heap()
# l = len(A)
# i = A.index(6)
# print('index:',i)
# print('len:',l)
# print(hp.is_leaf_node(i,l))

print(A)
# hp.heapify_down(i,A)
B = hp.make_heap(A)
print(B)
# B = [15, 12, 6, 11, 10, 2, 3, 1, 8]
#        15
#      /    \
#    12      6
#   /  \    /  \
#  11  10  2    3
# /  \ 
# 1   8

#'''


''' insert 
from my_heap import Heap

A = [2,8,6,1,10,15,3,12,11]
B = [15, 12, 6, 11, 10, 2, 3, 1, 8]
#        15
#      /    \
#    12      6
#   /  \    /  \
#  11  10  2    3
# /  \ 
# 1   8

hp = Heap()
hp.insert(14,B)
print('B: ', B)
# B = [15, 14, 6, 11, 12, 2, 3, 1, 8, 10]
#         15
#       /    \
#     14      6
#   /   \    /  \
#  11   12  2    3
# / \   / 
# 1  8 10 

#'''


''' delete_max find_max insert
from my_heap import Heap

A = [2,8,6,1,10,15,3,12,11]
#        2
#      /   \
#     8      6
#    / \    /  \
#   1  10  15   3
#  /  \
# 12  11

C = Heap(A)
# print(C.heap)
print('C: ', C)
C.insert(14)
print('C: ', C)
print(C.find_max())
print(C.delete_max())
print(C.delete_max())
print(C.delete_max())
print(C.delete_max())
print(C)
#'''


# ''' sort
from my_heap import Heap

A = [2,8,6,1,10,15,3,12,11]
#        2
#      /   \
#     8      6
#    / \    /  \
#   1  10  15   3
#  /  \
# 12  11

C = Heap(A)
print('C: ', C)
C.insert(14)
print('C: ', C)
print(C.sort())
print(C)
#'''


''' test
from my_heap import Heap

A = [2,8,6,1,10,15,3,12,11]
#        2
#      /   \
#     8      6
#    / \    /  \
#   1  10  15   3
#  /  \
# 12  11

print('A: ',A)
B = hp.make_heap(A)
print('A: ',A)
print('B: ', B)
#'''