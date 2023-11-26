class Stack:
  def __init__(self):
    self.items = []

  def push(self, val):
    self.items.append(val)

  def pop(self):
    try:
      return self.items.pop()
    except IndexError:
      print('Stack is empty')

  def top(self):
    try:
      return self.items[-1]
    except IndexError:
      print('Stack is empty')
      
  def __len__(self):
    return len(self.items)
  
  # 아래는 챗gpt 답변
  def is_empty(self):
    return len(self.items) == 0
  
  def pop2(self):
    if not self.is_empty():
      return self.items.pop()
    else: # 답변 코드에서 조건 추가
      print('Stack is empty')
  
  def peek(self): # 강의에서의 top(self)와 동일 
    if not self.is_empty():
      return self.items[-1]
    else: # 답변 코드에서 조건 추가 
      print('Stack is empty') 
  
s=Stack()
s.push(10)
s.push(2)

print(s.pop()) # 2
print(s.top()) # 10
print(len(s)) # 1