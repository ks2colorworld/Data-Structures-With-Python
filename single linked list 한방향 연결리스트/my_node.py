class MyNode:
  def __init__(self,key=None,value=None):
    self.key = key
    self.value = value
    self.next = None
  def nextNode(self,node=None):
    self.next = node
  def __str__(self):
    selfString = f'node[{str(self.key)}]'
    # nextString = '->@'
    # if self.next != None:
    #   nextString = f'->node[{str(self.next.key)}]'
    return f'{selfString}'
    # return f'{selfString}{nextString}'

'''
def f():
  pass
  print(1)

f()
'''