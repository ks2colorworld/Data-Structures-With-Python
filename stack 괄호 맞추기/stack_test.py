from stack import Stack

s=Stack()
s.push(10)
s.push(2)

print(s.pop()) # 2
print(s.top()) # 10
print(len(s)) # 1
print(s.pop2())
print(s.pop())
print(s.pop2())

print(s)