from stack import Stack

def check_match_brackets(str, show_steps=False):
    if show_steps : print(str)
    S=Stack()
    
    # 괄호의 짝을 맞추기 위한 매핑
    bracket_pairs = {')': '(', '}': '{', ']': '['}
    
    for p in str:
        # 시작 괄호 체크
        if p in "({[":
            S.push(p)
            if show_steps : print(f"push(p='{p}')")
        # 종료 괄호 체크
        elif p in ")}]":
            # 시작 괄호가 없으면 Error
            if S.is_empty():
                if show_steps : print(f"p='{p}' but stack is empty')")
                return False
            s = S.pop()
            if show_steps : print(f"p='{p}' pop()='{s}'")
            # 시작 괄호가 종료 괄호와 맞지 않으면 Error
            if s != bracket_pairs[p]:
                if show_steps : print(f"'{s}'!='{bracket_pairs[p]}'")
                return False
        # 시작/종료 괄호가 아닌 경우 다음으로 계속
        else :
            continue
        #   if show_steps : print(f"Not allowed Symbol p='{p}'")

    # 모든 괄호가 짝이 맞아야 True를 반환 (Error 없이 종료)
    return S.is_empty()

# # 테스트
# expression1 = "())(2 + 3) * 5)"
# expression2 = "{[1 + 2] * 4 - (3 / 2)}"
# expression3 = "((1 + 2) * 3}"
# str = '())'

# print(check_match_brackets(expression1,True))  # True
# print(check_match_brackets(expression2, True))  # True
# print(check_match_brackets(expression3,True))  # False
# print(check_match_brackets(str)) # False 