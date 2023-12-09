from queue import Queue
from my_queue import My_Queue

def josephus(n,k,q=None):
  print(f'n={n}, k={k}')
  # 1~n만큼의 숫자들 중 최종 남는 번호(숫자)
  num_final = 0
  # n,k 모두 1보다 큰 숫자인지 확인 >> 아니면 실행 중단
  if n <= 0 or k <= 0:
    print('required 0 < n and 0 < k')
    return num_final
  
  if q == None : q = Queue() # 특정 queue가 없으면 파이썬 기본 큐를 사용한다
  for i in range(n):
    q.put(i+1)
  print(list(q.queue)) 
  dequeue_max = k - 1
  while not q.empty():
    dequeue_count = 0
    while dequeue_count < dequeue_max:
      a = q.get()
      print('q.put(q.get()) = ', a)
      q.put(a)
      print(list(q.queue))
      dequeue_count += 1
      # queue에 숫자 하나만 남으면 진행을 종료한다
      if len(q.queue) == 1: break
    num_final = q.get()
    print('q.get() = ', num_final, '\n')
    
  print('num_final=', num_final)
  
  return num_final

n = 9
k = 3
# print(josephus(n,k)) 
q = My_Queue() # 강의 내용에서 구현한 queue 
print(josephus(n,k,q))