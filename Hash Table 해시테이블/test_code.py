'''
table = [1]*10
# print(table) # 1이 10만큼 저장된 list(array) # [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

index = 1
key = 10
value = "ten"

# table[index] = (key,value)
talbe[index] = [(key,value)]
print(table)
print(table[index])
print(table[index][0])
#'''


#'''
from my_hash_table1 import HashTable

ht = HashTable() # size : 10
ht.set(1,10)
ht.set(21,20)
ht.set(38,30)
ht.set(41,40)
ht.set(58,50)
ht.set(68,60)
ht.set(78,70)
# ht.set(88,800)
# ht.set(98,900)
ht.set(108,100)
# ht.set(208,200) # IndexError: not find slot
ht.set(308,300)
print(ht.table)
print(ht.search(78))
print(ht.search(1))
print(ht.search(308)) # None

print(ht.find_slot(108))

#'''
