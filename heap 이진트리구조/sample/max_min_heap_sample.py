import heapq

class HeapDataStructure:
    def __init__(self):
        self.data = []

    def add_element(self, element):
        heapq.heappush(self.data, element)

    def get_min(self):
        if not self.data:
            return None
        return self.data[0]

    def get_max(self):
        if not self.data:
            return None
        return max(self.data)

# 예시 사용법
my_heap_data_structure = HeapDataStructure()

# 데이터 추가
my_heap_data_structure.add_element(5)
my_heap_data_structure.add_element(10)
my_heap_data_structure.add_element(3)
my_heap_data_structure.add_element(8)

# 최소값 및 최대값 확인
min_value_heap = my_heap_data_structure.get_min()
max_value_heap = my_heap_data_structure.get_max()

print(f"최소값(힙): {min_value_heap}")
print(f"최대값(리스트): {max_value_heap}")
print(my_heap_data_structure.data)