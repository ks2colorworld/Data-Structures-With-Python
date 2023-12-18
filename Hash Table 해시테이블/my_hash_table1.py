class HashTable:
  def __init__(self, size=10) -> None:
    self.NOT_FIND_SLOT = -1
    self.table = [None]*size # None이 size 갯수(10)만큼 저장된 list(array)
    self.size = size # len(self.table)
  def __hash_function(self,key:int)->int: # Division hash function (나머지)
    k = key 
    m = self.size
    # P = 11
    # return (k%P)%m # 특정소수 P 11 (key%11) 
    # return hash(k)%m # 파이썬 제공 해시함수 
    return k%m 
  def __probe(self,index)->int: # open addressing : linear probing - move to the next slot
    return (index+1)%self.size
  def __is_collision(self,index,key:int)->bool: # Check if there is a collision at the specified index
    return self.__occupied(index) and self.__is_not_same_key(index,key) # self.table[index] != None and self.table[index][0] != key
  def __unoccupied(self,index)->bool:
    return self.table[index] == None
  def __occupied(self,index)->bool:
    return not self.__unoccupied(index)
  def __is_same_key(self,index,key=int)->bool:
    return self.table[index][0] == key
  def __is_not_same_key(self,index,key=int)->bool:
    return not self.__is_same_key(index,key)
  
  def find_slot(self,key:int)->int:
    i = self.__hash_function(key)
    start=i 
    while self.__is_collision(i,key): # 충돌(해당 i에 다른 key)이 일어나면 / 동일한 key의 slot(index)이 존재하면
      # print(i)
      i = self.__probe(i) # (i+1)%self.size / move to the next slot
      if i == start: # not find slot
        # raise IndexError("not find slot")
        return self.NOT_FIND_SLOT # -1
    return i 
  def set(self,key:int,value=None):
    i = self.find_slot(key)
    if i == self.NOT_FIND_SLOT: return None # hash table is full (TODO : Double self.table size )
    self.table[i] = (key,value) # replace value or insert value
    return key
  def search(self,key:int): 
    i = self.find_slot(key)
    if i == self.NOT_FIND_SLOT: return None # key does not exist
    if self.__occupied(i) and self.__is_same_key(i,key): # if self.table[i] != None and self.table[i][0] == key:
      return self.table[i][1] # value / key : self.table[i][0]
    else: return None
  def remove(self, key:int):
    '''
    1.이 키(key1)에 해당되는 slot(index1)을 찾는다 : find-slot(key1) - 찾으면 해당 slot의 index를 반환하고, 못 찾으면 set할 수 있는 slot의 index를 반환한다.
    2.찾은 slot(index1)의 키(key2)를 확인한다. 
    3.그 slot(index1)이 비어있는지, key1과 key2가 같은지 확인한다.
    4-1.(비어 있거나 다르다=못찾았다) 이 키(key1)은 없으므로 (remove 대상이 없으므로) 코드 진행을 종료한다.
    4-2.(비어 있지 않고 같다=찾았다) 이 slot(index1)을 비운다.
    5.이 다음 slot(index2)을 찾는다: probe(index1) - slot 중복 충돌발생시 그 다음 slot을 제공하는 함수를 실행한다는 의미
    6.그 slot(index2)가 비어 있는지 확인한다. unoccupied(index2)
    7-1.(비어 있다) find-slot(key1)로 찾은 맨마지막 slot(index1)을 비웠고(4-2.), 그 다음도 비어 있으므로 코드 진행을 종료한다.
    7-2.(비어 있지 않다) slot(index2)의 키값(key3)을 확인한다.
    8.이 키값(key3)이 저장될 원래 slot(index0)을 확인(index0=hash_function(key3))한 후 index0과 index1값과 같은지 확인한다.
    9-1.(같지 않다) probe()함수로 저장위치가 이동된 대상이 아니므로, 작업대상을 다음 slot(index3)으로 변경 후(5.probe(index2)) 6.부터 반복한다.
    9-2.(같다) slot(index1)에 slot(index2)의 key/value를 옮기고 slot(index2)를 비운 후(4-2.) 5.부터 반복한다.
    #'''
    H = self.table
    # 1.이 키(key)에 해당되는 slot(i)을 찾는다 : find-slot(key) - 찾으면 해당 slot의 index를 반환하고, 못 찾으면 set할 수 있는 slot의 index를 반환한다.
    i = self.find_slot(key)
    # 2.찾은 slot(i)의 키(key2)를 확인한다. 
    print('key:', key, ', i:',i, ', H[i]:',H[i])
    # 3.그 slot(i)이 비어있는지, key과 key2가 같은지 확인한다.
    # 4-1.(비어 있거나 다르다=못찾았다) 이 키(key)는 없으므로 (remove 대상이 없으므로) 코드 진행을 종료한다.
    if self.__unoccupied(i) or self.__is_not_same_key(i,key): return None # key does not exist
    j = i
    while True: 
      # 4-2.(비어 있지 않고 같다=찾았다) 이 slot(i)을 비운다.
      H[i] = None # remove H[i]
      print(self.table)
      while True: # find H[j]
        # 5.이 다음 slot(j)을 찾는다: probe(i==j) - slot 중복 충돌발생시 그 다음 slot을 제공하는 함수를 실행한다는 의미
        j = self.__probe(j)
        # 6.그 slot(j)가 비어 있는지 확인한다. unoccupied(j)
        # 7-1.(비어 있다) find-slot(key)로 찾은 맨마지막 slot(i)을 비웠고(4-2.), 그 다음도 비어 있으므로 코드 진행을 종료한다.
        if self.__unoccupied(j): return key # 삭제한 key값을 반환한 후 함수 종료
        # 7-2.(비어 있지 않다) slot(j)의 키값(j_key)을 확인한다.
        j_key=H[j][0] # H[j].key
        # 8.이 키값(j_key)이 저장될 원래 slot(k)을 확인(k=hash_function(j_key))한 후 k과 origin_slot_index값과 같은지 확인한다.
        k = self.__hash_function(j_key)
        print('j_key: ',j_key,', k: ', k)
        # 9-1.(같다) slot(i)에 slot(j)의 key/value를 옮기고 slot(j)를 비운 후(4-2.) 5.부터 반복한다.(4-2~)
        print(' k:',k,', H[j]:', H[j],', j:',j,', i:',i)
        # if k < i and i <= j: # 강의 내용 기준 
        if k < i and i <= j or \
          i <= j and j < k or \
          j < k and k <= i: # 강의 내용의 조건 추가 
          H[i] = H[j] # slot(i)에 slot(j)의 key/value를 옮기고
          print('move j to i- H[j]:',H[j],', i:',i,', j:',j)
          i = j # (while 반복문 상단에서) slot(j)를 비운다 (H[i] = None)
          print('delete H[j]:',H[i],', j(new i):',i)
          break 
        # 9-2.(같지 않다) probe()함수로 저장위치가 이동된 대상이 아니므로, 작업대상을 다음 slot(다음j)으로 변경 후(5.probe(j)) 6.부터 반복한다. (5~ )