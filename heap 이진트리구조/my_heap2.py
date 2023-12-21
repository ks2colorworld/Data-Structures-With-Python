import heapq

class Heap:
  def __init__(self,A:list=None) -> None:
    self.heap = self.make_heap(A)
  def __repr__(self) -> str: # self == self.heap
    max_heap = self.__return_max_list(self.heap)
    return repr(max_heap)
  def sort(self,A:list=None):
    H = None
    if A is None:
      H = self.heap
    else:
      H = self.make_heap(A)
    if H is None:
      return None
    H.sort(reverse=True)
    return self.__return_max_list(H)
  def insert(self,k:int,A:list=None): # BigO(log n)
    if A is None:
      A = self.heap
    heapq.heappush(A,-k)
  def find_max(self,A:list=None): # BigO(1)
    if A is None:
      A = self.heap
    else:
      A = self.make_heap(A)
    if A is None:
      return None
    return -A[0]
  def pop_max(self,A:list=None):
    return self.delete_max(self,A)
  def delete_max(self,A:list=None): # BigO(log n)
    if A is None:
      A = self.heap
    else:
      A = self.make_heap(A)
    if A is None:
      return None
    max_value = -heapq.heappop(A)
    return max_value
  def make_heap(self,A:list)->list: # BigO(n*t) - BigO(n*h) - BigO(n*log n) - BigO(n)
    if A is None:
      return None
    B = A.copy()
    max_heap = [-x for x in B]
    heapq.heapify(max_heap)
    # max_heap = [-x for x in max_heap]
    return max_heap
  def __return_max_list(self,A:list):
    max_heap = [-x for x in A]
    return max_heap