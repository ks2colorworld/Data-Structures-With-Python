import queue

class MyQueue:
    def __init__(self):
        self._queue = queue.Queue()

    def enqueue(self, item):
        self._queue.put(item)

    def dequeue(self):
        if not self.is_empty():
            return self._queue.get()
        else:
            print("Queue is empty")

    def is_empty(self):
        return self._queue.empty()

    def size(self):
        return self._queue.qsize()
    
    def get_values_as_list(self):
        return list(self._queue.queue)

# 사용 예시
my_queue = MyQueue()

my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

print("Queue values:", my_queue.get_values_as_list())

print("Queue size:", my_queue.size())

print("Dequeue:", my_queue.dequeue())
print("Dequeue:", my_queue.dequeue())
print("Dequeue:", my_queue.dequeue())

print("Is empty:", my_queue.is_empty())



