''' 기대와 다르게 작동함. 
import heapq

class DualHeap:
    def __init__(self):
      # 최대 힙 (Max Heap)
      self.max_heap_left = []

      # 최소 힙 (Min Heap)
      self.min_heap_right = []

    def insert(self, value):
      heapq.heappush(self.max_heap_left, -value)
      heapq.heappush(self.min_heap_right, value)

    def heappop_min(self):
      if not self.min_heap_right:
        raise IndexError("Cannot pop from an empty heap")

      min_value = heapq.heappop(self.min_heap_right)
      self._balance_heaps()
      return min_value

    def heappop_max(self):
      if not self.max_heap_left:
        raise IndexError("Cannot pop from an empty heap")

      max_value = -heapq.heappop(self.max_heap_left)
      self._balance_heaps()
      return max_value

    def _balance_heaps(self):
      # 두 힙의 크기 차이가 2 이상이면 균형을 맞춰줌
      if len(self.max_heap_left) > len(self.min_heap_right)+ 1:
        heapq.heappush(self.min_heap_right, -heapq.heappop(self.max_heap_left))
      elif len(self.min_heap_right) > len(self.max_heap_left):
        heapq.heappush(self.max_heap_left, -heapq.heappop(self.min_heap_right))

# 테스트
dual_heap = DualHeap()
dual_heap.insert(4)
dual_heap.insert(1)
dual_heap.insert(7)
dual_heap.insert(3)

print(dual_heap.min_heap_right)
print(dual_heap.max_heap_left)

# min_value = dual_heap.heappop_min()
print("Min Value:", dual_heap.heappop_min())  # Min Value: 1
print("Min Value:", dual_heap.heappop_min())  # Min Value: 3
# print("Min Value:", dual_heap.heappop_min())  # Min Value: 4
# print("Min Value:", dual_heap.heappop_min())  # Min Value: 7

print(dual_heap.min_heap_right)
print(dual_heap.max_heap_left)

max_value = dual_heap.heappop_max()
print("Max Value:", max_value)  # Max Value: 7

print(dual_heap.min_heap_right)
print(dual_heap.max_heap_left)
# '''