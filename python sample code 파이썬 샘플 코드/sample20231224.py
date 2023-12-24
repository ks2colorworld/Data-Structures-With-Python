'''
class A:
  def __init__(self,val1=0) -> None:
    self.val1=val1
    self.val2=val1*100
# '''

# """ 
class A:
  def __init__(self, val1=0) -> None:
    self.__val1 = val1
    self.__val2 = val1 * 100

  @property
  def val1(self):
    return self.__val1

  @val1.setter
  def val1(self, value):
    self.__val1 = value
    self.__val2 = value * 100

  @property
  def val2(self):
    return self.__val2
# """

x=A(2)
print(x.val1) # 2
print(x.val2) # 200

a=A()
a.val1=2 
print(a.val1) # 2
print(a.val2) # 100
