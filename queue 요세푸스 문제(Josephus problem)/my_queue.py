class My_Queue:
  def __init__(self):
    self.items = [] # 빈 리스트
    self.front_index = 0
    self.queue = self.items
  def enqueue(self, val):
    self.items.append(val)
  def dequeue(self):
    # if self.front_index == len(self.items):
    if self.is_empty():
      print('Q is empty')
      return None
    x = self.items[self.front_index]
    self.front_index += 1
    return x
  
  # 강의 내용 이외
  def is_empty(self):
    return self.front_index == len(self.items)
  def __len__(self):
    return len(self.items) - self.front_index
  def __str__(self):
    list_string = ','.join(map(str, self.items)) # 숫자/문자열 
    return 'queue(['+list_string+'])'
  
  # 호환을 위해 추가
  def put(self,val):
    self.enqueue(val)
  def get(self):
    return self.dequeue()
  def empty(self):
    return self.is_empty()
  