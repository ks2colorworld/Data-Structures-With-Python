from stack import Stack

def check_match_brackets(str, show_steps=False):
  if show_steps : print(str)
  
  S=Stack()
  parSeq = str # '(2+5)*7-((3-1)/2+7)'
  for p in parSeq:
    if p == '(' :
      S.push(p)
      if show_steps : print(f"push('{p}')")
    elif p== ')':
      if len(S) == 0:
        return False # str = '())' # false 
      else :
        S.pop()
      if show_steps : print(f"p='{p}' pop()")
    else : 
      if show_steps : print(f"Not allowed Symbol '{p}'")

  if len(S) > 0: return False
  else: return True
