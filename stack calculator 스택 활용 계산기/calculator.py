import string
import sys
sys.path.append('../stack 괄호 맞추기')
from stack import Stack
from match_gpt import check_match_brackets

# infix 형식으로 작성된 표현식을 받아서 
# postfix 형식으로 변경하여 넘겨주는 함수 
# 제한 1 : 한자리 수의 피연산자로 제한 
# 제한 2 : 단항연산자(음수/양수 표시)는 고려하지 않는다
def change_to_postfix(infix_string, show_steps=False):
  # 넘어온 문자열을 출력하여 표시한다.(확인용)
  if show_steps : print('infix : ', infix_string)
  
  # 넘어온 문자열의 괄호가 올바르게 되어 있는지 우선 확인한다
  if show_steps : print('Check match brackets first')
  if not check_match_brackets(infix_string, show_steps):
    if show_steps : show_steps_message('error', 'brackets are mismatched')
    raise ValueError(f"brackets are mismatched")
    return None
  if show_steps : print('Verified brackets are matched')
  
  # 괄호의 짝을 맞추기 위한 매핑
  bracket_pairs = {')': '(', '}': '{', ']': '['}
  
  # (추가-여러자리 숫자 처리를 위한 조치) 이전 토큰이 숫자였는지 여부를 저장한다.
  previous_token_is_number = False
  # postfix로 변경되어 저장될 Stack(1-postfix)을 준비한다. 
  stack_for_postfix = Stack()
  # postfix로 변경하기 전 피연산자들의 우선순위에 따라 임시 저장할 Stack(2-operator)을 준비한다.
  stack_for_operator = Stack()
  
  # infix_string의 첫번째 문자열(토큰이라 한다)부터 맨마지막 문자열까지 차례대로 아래 작업(3)을 반복한다
  token_index = 0
  while token_index < len(infix_string):
    current_token = infix_string[token_index]
    if show_steps : print('current_token : ', current_token)

    # 토큰이 ,(천단위 구분 문자열)이면
    # if current_token == ',':
    #   token_index += 1
    #   continue
    
    # 토큰이 피연산자(숫자)이면 
    if current_token.isdigit():
      # (추가-여러자리 숫자 처리를 위한 조치) 이전 토큰이 숫자였으면 
      # stack_for_postfix.pop해서 현재 토큰을 문자열로 연결하여 붙인 후 다시 push한다.
      if previous_token_is_number:
        p_number = stack_for_postfix.pop()
        current_token = p_number+current_token
      # 해당 토큰을 Stack(1-postfix)에 push하고 아래 작업은 더이상 실행하지 않고 다음 토큰에 대한 작업(3)을 다시 진행한다 
      stack_for_postfix.push(current_token)
      previous_token_is_number = True
      if show_steps : show_steps_message('1', stack_for_postfix, stack_for_operator)
      token_index += 1
      continue
    
    # 토큰이 '(' 이면
    if current_token in "({[": # == '(':
      # 해당 토큰을 Stack(2-operator)에 push하고 아래 작업은 더이상 실행하지 않고 다음 토큰에 대한 작업(3)을 다시 진행한다 
      stack_for_operator.push(current_token)
      if show_steps : show_steps_message('2', stack_for_postfix, stack_for_operator)
      token_index += 1
      continue
    
    # 토큰이 ')' 이면
    if current_token in ")}]": # == ')':
      repeat_condition = True
      # 아래 작업(4)을 중단될 때까지 반복한다
      while repeat_condition:
        try:
          # Stack(2-operator)를 pop한다
          op = stack_for_operator.pop()
          # pop된 연산자가 '('이면
          if op == bracket_pairs[current_token]: # '(':
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
      if show_steps : show_steps_message('3', stack_for_postfix, stack_for_operator)
      token_index += 1
      continue
    
    # 토큰이 ')' 이면
    if current_token in ('+','-','*','/'):
      # (추가-여러자리 숫자 처리를 위한 조치) 현재 토큰이 연산자이면 다음 토큰 처리시 현재 토큰이 연산자였음(숫자가 아님)을 알리기 위한 플래그를 남긴다. 
      previous_token_is_number = False
      # (추가) stack_for_operator이 비어 있으면 현재 토큰을 push하고 다음 토큰에 대한 작업(3)을 다시 진행한다 
      if stack_for_operator.is_empty():
        stack_for_operator.push(current_token)
        if show_steps : show_steps_message('4', stack_for_postfix, stack_for_operator)
        token_index += 1
        continue
      # 토큰의 우선순위에 따라 아래 작업(5)을 반복한다
      repeat_condition = True
      while repeat_condition:
        # 토큰 '*','/'의 우선순위는 '+','-'의 우선순위보다 높다 
        # Stack(2-operator)의 top을 확인하고 토큰과의 우선순위를 비교한다 
        top_operator = stack_for_operator.top()
        pop_condition = top_operator in ('*','/') # todo : 조건 검정할 것 ok
        # Stack(2-operator)의 top의 우선순위가 토큰보다 높거나 같으면 
        if pop_condition:
          # Stack(2-operator)를 pop하여 Stack(1-postfix)에 push한다
          stack_for_postfix.push(stack_for_operator.pop())
          if show_steps : show_steps_message('5-1', stack_for_postfix, stack_for_operator)
          # 작업(5)를 다시 진행한다
          continue
        # Stack(2-operator)의 top의 우선순위가 토큰보다 낮으면 
        else:
          # 해당 토큰을 Stack(2-operator)에 push한다 
          stack_for_operator.push(current_token)
          if show_steps : show_steps_message('5-2', stack_for_postfix, stack_for_operator)
          # 작업(5)을 중단한다
          repeat_condition = False
          break
        
    # 아래 작업은 더이상 실행하지 않고 다음 토큰에 대한 작업(3)을 다시 진행한다 
    # if show_steps : show_steps_message('5-3', stack_for_postfix, stack_for_operator)
    token_index += 1
    # continue
  
  # Stack(2-operator)의 top이 있을 때까지 작업(6)을 반복한다
  while not stack_for_operator.is_empty():
    # Stack(2-operator)를 pop한 후 Stack(1-postfix)에 push한다
    stack_for_postfix.push(stack_for_operator.pop())
    if show_steps : show_steps_message('last(7)', stack_for_postfix, stack_for_operator)
    
  
  # infix형식으로 넘어온 문자열이 전부 postfix로 변경되면
  # Stack(1-postfix)을 넘겨주고 함수실행을 종료한다
  return stack_for_postfix

def calculate_postfix(stack_postfix:Stack, show_steps=False):
  if show_steps : print('postfix : ', stack_postfix)
  # 피연산자 스택 준비
  stack_for_operand = Stack()
  # 계산완료 결과값
  cal_result = 0
  # postfix의 첫번째 문자열(토큰이라 부른다)부터 마지막 문자열까지 아래 작업(1)을 반복한다
  token_index = 0
  while token_index < len(stack_postfix):
    current_token = stack_postfix[token_index]
    # 토큰이 피연산자이면
    if current_token.isdigit():
      # 피연산자 스택에 push한다
      stack_for_operand.push(current_token)
      token_index += 1
      continue
    
    # 토큰이 연산자이면
    if current_token in ('+','-','*','/'):
      # (예외 추가) 피연산자가 2개이상 남아 있지 않으면 오류
      if len(stack_for_operand) < 2:
        raise ValueError(f"error : operands count < 2 ")
        break
      # 피연산자 스택에서 두번 pop한 후 
      # 첫번째 pop은 오른쪽 / 두번째 pop은 왼쪽 
      right_operand = float(stack_for_operand.pop())
      left_operand = float(stack_for_operand.pop())
      temp_result = 0
      # 두 피연산자를 연산자로 계산한다
      if current_token == '+':
        temp_result = left_operand + right_operand
      elif current_token == '-':
        temp_result = left_operand - right_operand
      elif current_token == '*':
        temp_result = left_operand * right_operand
      elif current_token == '/':
        temp_result = left_operand / right_operand
      # 계산한 결과값을 피연산자 스택에 push한다
      stack_for_operand.push(temp_result)
      token_index += 1
      continue
    
  cal_result = stack_for_operand.pop()
  return cal_result

# change_to_postfix() + calculate_postfix()
def calulate_infix(infix_string:string, show_steps=False, *, with_comma=False):
  cal_result = calculate_postfix(change_to_postfix(infix_string, show_steps), show_steps)
  return add_comma(cal_result) if with_comma else cal_result

def show_steps_message(title_string, *steps_message):
  print(f'----{title_string}----')
  if len(steps_message) <= 0: return
  for msg in steps_message:
    print(msg)
  return

# add comma
def add_comma(num:int|float):
  return f"{num:,}"

def remove_comma(string_num:string):
  clean_string = string_num.replace(',','')
  if '.' in string_num:
    return float(clean_string)
  else:
    return int(clean_string)
