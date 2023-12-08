import sys
sys.path.append('../stack Folder') # blank folder에서 실행시
# sys.path.append('./stack Folder') # 상위 폴더에서 실행시
from stack import Stack
from match import check_match_brackets

s=Stack()
s.push(10)
s.push(2)

print(s.pop()) # 2
print(s.top()) # 10
print(len(s)) # 1
print(s.pop2())
print(s.pop())
print(s.pop2())

str = '(2+5)*7-((3-1)/2+7)'
str = '())' # false 
print(check_match_brackets(str))


# blank Folder 폴더 내에서 실행 
# ~/root/blank folder
# ❯ python3 include_blank_char_folder.py

# 폴더 위치가 다를 경우 경로 오류 발생 >> 실행되는 폴더위치에 맞춰서 경로변경시 실행가능
# ~/root
# ❯ python3 "./blank Folder/include_blank_char_folder.py"

''' 폴더 경로 설명 
- root
  - stack Folder
    - stack.py
    - match.py
  - blank Folder
    - include_blank_char_folder.py
'''