from collections import deque
from queue import Queue
from my_queue import My_Queue

#####

de = deque([4,5,6])
de.appendleft(3)
de.append(7)

print(de) # deque([3, 4, 5, 6, 7])
print(list(de)) # [3, 4, 5, 6, 7]

print(de.pop()) # 7
print(de.popleft()) # 3

print(de) # deque([4, 5, 6])

#####

qe = Queue()
qe.put(4)
qe.put(5)
qe.put(6)

print(list(qe.queue)) # [4, 5, 6]

print(qe.get()) # 4
print(qe.get()) # 5
print(qe.get()) # 6

#####

mqe = My_Queue()
mqe.enqueue(4)
mqe.enqueue(5)
mqe.enqueue(6)

print(mqe) # queue([4,5,6])

print(mqe.dequeue()) #4
print(mqe.dequeue()) #5
print(mqe.dequeue()) #5