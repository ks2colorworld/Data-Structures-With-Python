
current_token = '10'
# current_token = '-10'

if current_token.lstrip('-').isdigit():
  print('Yes')
else:
  print('No')