import sys
sys.path.append('../stack 괄호 맞추기')
from stack import Stack

# infix 형식으로 작성된 표현식을 받아서 
# postfix 형식으로 변경하여 넘겨주는 함수 
# 제한 1 : 한자리 수의 피연산자로 제한 
# 제한 2 : 단항연산자(음수/양수 표시)는 고려하지 않는다
def change_to_postfix(infix_string):
  # 넘어온 문자열을 출력하여 표시한다.(확인용)
  print('infix : ', infix_string)
  # postfix로 변경되어 저장될 Stack(1-postfix)을 준비한다. 
  stack_for_postfix = Stack()
  # postfix로 변경하기 전 피연산자들의 우선순위에 따라 임시 저장할 Stack(2-operator)을 준비한다.
  stack_for_operator = Stack()
  
  # infix_string의 첫번째 문자열(토큰이라 한다)부터 맨마지막 문자열까지 차례대로 아래 작업(3)을 반복한다
  token_index = 0
  while token_index < len(infix_string):
    current_token = infix_string[token_index]
    print('current_token : ', current_token)
    # 토큰이 피연산자(숫자)이면 
    if current_token.isdigit():
      # 해당 토큰을 Stack(1-postfix)에 push하고 아래 작업은 더이상 실행하지 않고 다음 토큰에 대한 작업(3)을 다시 진행한다 
      stack_for_postfix.push(current_token)
      print('----1----')
      print(stack_for_postfix)
      print(stack_for_operator)
      token_index += 1
      continue
    
    # 토큰이 '(' 이면
    if current_token == '(':
      # 해당 토큰을 Stack(2-operator)에 push하고 아래 작업은 더이상 실행하지 않고 다음 토큰에 대한 작업(3)을 다시 진행한다 
      stack_for_operator.push(current_token)
      print('----2----')
      print(stack_for_postfix)
      print(stack_for_operator)
      token_index += 1
      continue
    
    # 토큰이 ')' 이면
    if current_token == ')':
      repeat_condition = True
      # 아래 작업(4)을 중단될 때까지 반복한다
      while repeat_condition:
        try:
          # Stack(2-operator)를 pop한다
          op = stack_for_operator.pop()
          # pop된 연산자가 '('이면
          if op == '(':
            # 작업(4)을 중단한다
            repeat_condition = False
            break
          # pop된 연산자를 Stack(1-postfix)에 push하고 작업(4)을 다시 진행한다
          stack_for_postfix.push(op)
          continue
        # pop할 연산자가 없다면
        except ValueError as e:
          # 작업(4)을 중단하고 오류 처리한다 + 작업(3)도 중단한다
          raise ValueError(f"stack_for_operator : {e}")
          # repeat_condition = False
          # break
      # 작업(4)이 오류없이 중단되었으면 아래 작업은 더이상 실행하지 않고 다음 토큰에 대한 작업(3)을 다시 진행한다 
      print('----3----')
      print(stack_for_postfix)
      print(stack_for_operator)
      token_index += 1
      continue
    
    # 토큰이 ')' 이면
    if current_token in ('+','-','*','/'):
      # (추가) stack_for_operator이 비어 있으면 현재 토큰을 push하고 다음 토큰에 대한 작업(3)을 다시 진행한다 
      if stack_for_operator.is_empty():
        stack_for_operator.push(current_token)
        print('----4----')
        print(stack_for_postfix)
        print(stack_for_operator)
        token_index += 1
        continue
      # 토큰의 우선순위에 따라 아래 작업(5)을 반복한다
      repeat_condition = True
      while repeat_condition:
        # 토큰 '*','/'의 우선순위는 '+','-'의 우선순위보다 높다 
        # Stack(2-operator)의 top을 확인하고 토큰과의 우선순위를 비교한다 
        top_operator = stack_for_operator.top()
        pop_condition = top_operator in ('*','/') # todo : 조건 검정할 것 
        # Stack(2-operator)의 top의 우선순위가 토큰보다 높거나 같으면 
        if pop_condition:
          # Stack(2-operator)를 pop하여 Stack(1-postfix)에 push한다
          stack_for_postfix.push(stack_for_operator.pop())
          # 작업(5)를 다시 진행한다
          continue
        # Stack(2-operator)의 top의 우선순위가 토큰보다 낮으면 
        else:
          # 해당 토큰을 Stack(2-operator)에 push한다 
          stack_for_operator.push(current_token)
          # 작업(5)을 중단한다
          repeat_condition = False
          break
        
    # 아래 작업은 더이상 실행하지 않고 다음 토큰에 대한 작업(3)을 다시 진행한다 
    print('----5----')
    print(stack_for_postfix)
    print(stack_for_operator)
    token_index += 1
    # continue
  
  # Stack(2-operator)의 top이 있을 때까지 작업(6)을 반복한다
  while not stack_for_operator.is_empty():
    # Stack(2-operator)를 pop한 후 Stack(1-postfix)에 push한다
    stack_for_postfix.push(stack_for_operator.pop())
    print('----6----')
    print(stack_for_postfix)
    print(stack_for_operator)
    
  
  # infix형식으로 넘어온 문자열이 전부 postfix로 변경되면
  # Stack(1-postfix)을 넘겨주고 함수실행을 종료한다
  return stack_for_postfix




# str = '1+2*3' # 123*+
# str = '(1*2)+3' # 12*3+
# str = '(1+2)*3' # 12+3*
str = '(1+2)+3*4/5+(6*7-8)' # ?? 
print(change_to_postfix(str))