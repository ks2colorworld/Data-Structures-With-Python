import sys
sys.path.append('../single linked list 한방향 연결리스트')

from my_singly_linked_list import MySinglyLinkedList
from my_node import MyNode

class HashTableC:
  def __init__(self,size=10) -> None:
    self.table = [None]*size
    self.size = size
  def __hash_function(self,key):
    return hash(key)%self.size # 파이썬 제공 해시함수 
  def find_slot(self,key)->MySinglyLinkedList:
    slot_index = self.__hash_function(key)
    if self.table[slot_index] is None:
      newSlot = MySinglyLinkedList()
      self.table[slot_index] = newSlot
      return newSlot # 비어있는 슬롯 - 한방향연결리스트
    if not isinstance(self.table[slot_index], MySinglyLinkedList):
      raise TypeError(f"H[{slot_index}] is not SinglyLinkedList")
      return None
    return self.table[slot_index] # 한방향연결리스트 MySinglyLinkedList
  def set(self,key,value):
    slot = self.find_slot(key)
    # node = MyNode(key,value)
    slot.pushFront(key,value)
  def search(self,key)->MyNode|None:
    slot = self.find_slot(key)
    node = slot.search(key)
    if not isinstance(node, MyNode):
      raise TypeError("is not MyNode instance")
      return None
    if node is None:
      return None
    return node
  def remove(self,key):
    slot = self.find_slot(key)
    node = slot.delete(key)
    return node