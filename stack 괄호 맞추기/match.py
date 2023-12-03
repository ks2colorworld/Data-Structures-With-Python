from stack import Stack

def check_match_brackets(str):
  S=Stack()
  parSeq = str # '(2+5)*7-((3-1)/2+7)'
  for p in parSeq:
    if p == '(' :
      S.push(p)
      print(f"push('{p}')")
    elif p== ')':
      S.pop()
      print(f"p='{p}' pop()")
    else : 
      print(f"Not allowed Symbol '{p}'")

  if len(S) > 0: return False
  else: return True

str = '(2+5)*7-((3-1)/2+7)'
print(check_match_brackets(str))