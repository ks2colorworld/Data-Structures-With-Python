''' 힙 자료구조로 최소값 최대값을 같이 구현하는 것은 비효율적이다
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
      min_value = heapq.heappop(self.min_heap_right)
      
      self.max_heap_left = [] # 최대 힙 (Max Heap)
      for value in self.min_heap_right:
        heapq.heappush(self.max_heap_left, -value) # 비효율적?

      return min_value

    def heappop_max(self):
      max_value = -heapq.heappop(self.max_heap_left)

      self.min_heap_right = [] # 최소 힙 (Min Heap)
      for value in self.max_heap_left:
        heapq.heappush(self.min_heap_right, -value) # 비효율적?

      return max_value

# 테스트
dual_heap = DualHeap()
dual_heap.insert(4)
dual_heap.insert(1)
dual_heap.insert(7)
dual_heap.insert(3)

print(dual_heap.min_heap_right)

min_value = dual_heap.heappop_min()
print("Min Value:", min_value)  # Min Value: 1
print(dual_heap.min_heap_right)

max_value = dual_heap.heappop_max()
print("Max Value:", max_value)  # Max Value: 7
print(dual_heap.min_heap_right)
# '''