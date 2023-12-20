class Heap:
  def __init__(self,A:list=None) -> None:
    self.heap = self.make_heap(A)
  def __repr__(self) -> str: # self == self.heap
    return repr(self.heap)
  def insert(self,k:int,A:list=None): # BigO(log n)
    if A is None:
      A = self.heap
    A.append(k)
    if 0 < len(A):
      self.heapify_up(len(A)-1,A)
  def heapify_up(self,k:int,A:list): # BigO(log2 n)
    parent=(k-1)//2
    print('k:',k,', parent:',parent)
    while 0 < k and A[parent] < A[k]:
      P = A[parent]
      A[parent] = A[k]
      A[k] = P
      k = parent
      parent = (k-1)//2
  def find_max(self,A:list=None): # BigO(1)
    if A is None:
      A = self.heap
    else:
      A = self.make_heap(A)
    if A is None:
      return None
    return A[0]
  def pop_max(self,A:list=None):
    return self.delete_max(self,A)
  def delete_max(self,A:list=None): # BigO(log n)
    if A is None:
      A = self.heap
    else:
      A = self.make_heap(A)
    if A is None:
      return None
    a = A[0]
    A[0] = A[-1]
    A[-1] = a
    A.pop()
    self.heapify_down(0,A)
    return a # A[-1]
  def make_heap(self,A:list)->list: # BigO(n*t) - BigO(n*h) - BigO(n*log n) - BigO(n)
    B = A
    if B is None:
      return B
    n = len(B)
    # for (k = n-1; 0 <= k; k-- ) {/*pass*/} # js
    for k in range(n-1,-1,-1): # k = n-1,n-2, ..., 0
      # B[k] -> heap 성질을 만족하는 곳으로 서로 자리바뀜 
      self.heapify_down(k,B)
    return B
  def heapify_down(self,k:int,A:list): # BigO(h) - BigO(log n) 
    n = len(A)
    # A[k], n 
    while self.__is_not_leaf_node(k,n):
      K = A[k] 
      l = 2 * k + 1
      L = A[l]
      r = 2 * k + 2
      R = None
      if r<n:
        R = A[r]
      m = self.__index_max(K,L,R,k,l,r)
      if k != m:
        M = A[m]
        A[m] = K
        A[k] = M
        k=m
      # k+=1
      else:
      # if not(k < n):
        break
  def __is_leaf_node(self,index, total_nodes):
    return not self.__is_not_leaf_node(index,total_nodes)
  def __is_not_leaf_node(self,index, total_nodes):
    left_child = 2 * index + 1
    right_child = 2 * index + 2
    # print('index:', index, ', left child:', left_child, ', right child:', right_child)
    return left_child < total_nodes or right_child < total_nodes
  def __index_max(self,K,L,R,k,l,r):
    m = k 
    if K < L and (R is None or R <= L):
      m = l 
    elif R is not None and K < R and L < R: 
      m = r 
    return m