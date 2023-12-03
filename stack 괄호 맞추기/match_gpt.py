from stack import Stack

def check_brackets(expression):
  print(expression)
  S=Stack()
  
  # 괄호의 짝을 맞추기 위한 매핑
  bracket_pairs = {')': '(', '}': '{', ']': '['}
  
  for char in expression:
      if char in "({[":
          S.push(char)
      elif char in ")}]":
          if S.is_empty() or S.pop() != bracket_pairs[char]:
              return False

  # 모든 괄호가 짝이 맞아야 True를 반환
  return S.is_empty()

# 테스트
expression1 = "((2 + 3) * 5)"
expression2 = "{[1 + 2] * 4 - (3 / 2)}"
expression3 = "((1 + 2) * 3"
str = '())'

print(check_brackets(expression1))  # True
print(check_brackets(expression2))  # True
print(check_brackets(expression3))  # False
print(check_brackets(str)) # False 