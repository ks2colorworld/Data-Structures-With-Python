import heapq

print('---min---')
# """ 이 코드에서는 heapq 모듈의 heappush 함수를 사용하여 힙에 값을 추가하고, heappop 함수를 사용하여 최소값을 제거하고 반환합니다.
# 빈 힙 생성
heap = []

# 원소 추가
heapq.heappush(heap, 10)
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
heapq.heappush(heap, 5)

print("Min Heap:", heap)

# 최소값 접근 및 삭제
min_value = heapq.heappop(heap)
print("Min Value:", min_value)
print("Heap after pop:", heap)

min_value = heapq.heappop(heap)
print("Min Value:", min_value)
print("Heap after pop:", heap)

min_value = heapq.heappop(heap)
print("Min Value:", min_value)
print("Heap after pop:", heap)


# """

print('---max---')
# """ 최대 힙을 구현하려면, 각 값을 음수로 변환하여 넣고, 값을 뺄 때 다시 음수로 변환해야 합니다
# 빈 힙 생성
max_heap = []

# 원소 추가 (음수로 변환하여 추가)
heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -4)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -7)
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -5)

print("Max Heap(-):", max_heap)
print("Max Heap:", [-x for x in max_heap])

# 최대값 접근 및 삭제 (다시 음수로 변환)
max_value = -heapq.heappop(max_heap)
print("Max Value:", max_value)
print("Heap after pop:", [-x for x in max_heap])
print("Heap after pop(-):", max_heap)

max_value = -heapq.heappop(max_heap)
print("Max Value:", max_value)
print("Heap after pop:", [-x for x in max_heap])
print("Heap after pop(-):", max_heap)

max_value = -heapq.heappop(max_heap)
print("Max Value:", max_value)
print("Heap after pop:", [-x for x in max_heap])
print("Heap after pop(-):", max_heap)

max_value = -heapq.heappop(max_heap)
print("Max Value:", max_value)
print("Heap after pop:", [-x for x in max_heap])
print("Heap after pop(-):", max_heap)
# """