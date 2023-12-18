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





'''

from my_hash_table1 import HashTable

ht = HashTable() # size : 10

ht.set(2,'A2')
ht.set(3,'A3')
ht.set(102,'B2')
ht.set(5,'A5')
ht.set(105,'B5')
ht.set(10102,'C2')
ht.set(9,'A9')
ht.set(109,'B9')

# ht.set(10109,'C9')
# ht.set(1010109,'D9')


print(ht.table)

key = 3 # A3
key2 = 102 # B2
print(f'ht.remove({key})')
print('remove key : ',ht.remove(key))
print(ht.table)
print(ht.search(key2))

# print(ht.search(1010109))

# key = 9 # A9
# key2 = 109 # B9
# print(f'ht.remove({key})')
# print('remove key : ',ht.remove(key))
# print(ht.table)
# print(ht.search(key2))

#'''





'''
from my_hash_table1 import HashTable

ht = HashTable() # size : 10
ht.set(1,10)
ht.set(21,20)
ht.set(38,30)
ht.set(41,40)
ht.set(54,50)
ht.set(68,60)
ht.set(78,70)
ht.set(88,800)
ht.set(98,900)
ht.set(108,100)
# ht.set(208,200) # IndexError: not find slot
ht.set(307,300)
print(ht.table)
# print(ht.search(78))
# print(ht.search(1))
# print(ht.search(308)) # None

# print(ht.find_slot(108))

key = 88
key2 = 98
print(f'ht.remove({key})')
print('remove key : ',ht.remove(key))
print(ht.table)
print(ht.search(key2))
#'''





# '''
from chaning_hash_table import HashTableC

ht = HashTableC() # size : 10

ht.set(2,'A2')
ht.set(3,'A3')
ht.set(102,'B2')
ht.set(5,'A5')
ht.set(105,'B5')
ht.set(10102,'C2')
ht.set(9,'A9')
ht.set(109,'B9')

ht.set(10109,'C9')
ht.set(1010109,'D9')

print(ht.table[2])

key = 2 # A2
key2 = 102 # B2
print(f'ht.remove({key})')
print('remove key : ',ht.remove(key))
print(ht.table[2])
print(ht.search(key2).value)

print(ht.search(1010109).value)
print(ht.table[9])

# key = 9 # A9
# key2 = 109 # B9
# print(f'ht.remove({key})')
# print('remove key : ',ht.remove(key))
# print(ht.table)
# print(ht.search(key2))

#'''