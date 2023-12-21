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


''' sort
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
# from my_heap import Heap
from my_heap2 import Heap

A = [2,8,6,1,10,15,3,12,11]
#        2
#      /   \
#     8      6
#    / \    /  \
#   1  10  15   3
#  /  \
# 12  11

# B = A.copy()
# B.append(10)
# print(A)
# print(B)

# hp = Heap()
# print('A:',A)
# B = hp.make_heap(A)
# print('A:',A)
# print('B:',B)
# D = hp.sort(A)
# print('D:',D)
# print('A:',A)

C = Heap(A)
print('C:',C)
# print('A:',A)
print(C.insert(14))
print('C:',C)
print(C.sort())
# E=[23,1,234,4,53,32,445,32,56,78]
# print(C.sort(E))
print('C:',C)
# print('E:',E)


#'''

# '''
import heapq


A = [2,8,6,1,10,15,3,12,11]
#        2
#      /   \
#     8      6
#    / \    /  \
#   1  10  15   3
#  /  \
# 12  11


print('A:',A)
# heapq.heapify(A) # heap_min not max
# print('A:',A)
# # print(heapq.heappop(A))
# print(heapq.heapreplace(A,14)) # 힙 사이즈 유지 root node 제거 후 heappush
# # print(heapq.heappush(A,14))
# print(heapq.heappushpop(A,14)) # heappop() 후에 heappush(14)
# print('A:',A)
# heapq.heapify(A)
# print('A:',A)
# heapq._heapify_max(A)
# print('A:',A)
# print(heapq.heappop(A))
# heapq._heapify_max(A)
A.sort()
A.reverse()
print(A.pop())
B = [100,200,300,-10,-20,-30]
A.extend(B)
# heapq.heapify(A)
# heapq._heapify_max(A)
A.sort()
print(A.pop())
# A.reverse()
print('A:',A)

my_list = ["apple", "banana", "orange", "kiwi", '한글', '바나나','바나나바나나바']
my_list.sort(key=len, reverse=True)

print(my_list)
#'''


'''
def example_function(arg1, *, key_arg1=None, key_arg2=None):
    print("arg1:", arg1)
    print("key_arg1:", key_arg1)
    print("key_arg2:", key_arg2)

# 함수 호출
example_function("positional_argument", key_arg1="value1", key_arg2="value2")

# 오류 발생: example_function() missing 1 required positional argument: 'arg1'
# example_function("positional_argument111", "value1", "value2")
#'''