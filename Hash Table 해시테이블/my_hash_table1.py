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
    return self.table[index] != None and self.table[index][0] != key
  
  def find_slot(self,key:int)->int:
    i = self.__hash_function(key)
    start=i 
    while self.__is_collision(i,key):
      # print(i)
      i = self.__probe(i) # (i+1)%self.size
      if i == start: 
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
    if self.table[i] != None:
      return self.table[i][1] # value / key : self.table[i][0]
    else: return None
  def remove(self, key):
    pass