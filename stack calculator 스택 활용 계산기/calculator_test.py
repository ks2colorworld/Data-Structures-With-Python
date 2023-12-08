from calculator import change_to_postfix

# str = '1+2*3' # 123*+
# str = '(1*2)+3' # 12*3+
# str = '(1+2)*3' # 12+3*
str = '(1+2)+3*4/5+(6*7-8)' # 12+34*5/67*8-++ # 39.4
# print(change_to_postfix(str, True))
print('postfix : ', change_to_postfix(str, False))