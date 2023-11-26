def gcd(a,b):
  print('a : ',a)
  print('b : ',b)
  whileIndex=0 # while문 반복 횟수 
  
  while a!=0 and b != 0:
    if a>b: a= a%b
    else: b=b%a
    whileIndex += 1
    
  print('while count : ', whileIndex)
  return a+b

result = f'최대공약수 gcd : {gcd(2,100)}'

print(result)